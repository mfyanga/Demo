#include <QDebug>

#include "thread_tool.h"


// 构造函数只启动一些工作线程（worker）
ThreadPool::ThreadPool(std::size_t max_num)
    :   stop_(false)
{
    for(std::size_t i = 0; i<max_num; ++i)
        workers_.emplace_back(
            [this]
            {
                for(;;)
                {
                    std::function<void()> task;

                    {
                        std::unique_lock<std::mutex> lock(this->queue_mutex_);
                        this->condition_.wait(lock,
                            [this]{ return this->IsStop() || !this->IsIdle(); });

                        if(this->IsStop() && this->IsIdle()){
                            return;
                        }

                        task = std::move(this->tasks_.front());
                        this->tasks_.pop();
                    }

                    try {
                        task();
                    } catch (const std::exception& e) {
                        std::string error_info = "Exception in thread pool task: ";
                        error_info += e.what();
                        QString qstr = QString::fromStdString(error_info);
                        qDebug() << qstr;
                    }
                }
            }
        );
}

// 析构函数加入所有线程
ThreadPool::~ThreadPool()
{
    {
        std::unique_lock<std::mutex> lock(queue_mutex_);
        stop_ = true;
    }

    condition_.notify_all();
    for(std::thread &worker: workers_){
        worker.join();
    }
}
