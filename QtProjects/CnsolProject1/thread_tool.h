#ifndef THREAD_TOOL_H
#define THREAD_TOOL_H
#include <vector>
#include <queue>
#include <memory>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <future>
#include <functional>
#include <stdexcept>
//#include <atomic>

class ThreadPool {
public:
    ThreadPool(std::size_t max_num);

    template<class F, class... Args>
    auto enqueue(F&& f, Args&&... args)
        -> std::future<typename std::result_of<F(Args...)>::type>;

    ~ThreadPool();

private:
    bool IsStop() const {
        return stop_;
    }

    bool IsIdle() const {
        return tasks_.empty();
    }

private:
    // 需要保持跟踪线程以便可以加入它们
    std::vector<std::thread> workers_;

    // 任务队列
    std::queue<std::function<void()>> tasks_;

    // 同步
    std::mutex queue_mutex_;
    std::condition_variable condition_;
    bool stop_;
};


// 添加新的工作项到线程池
template<class F, class... Args>
auto ThreadPool::enqueue(F&& f, Args&&... args)
    -> std::future<typename std::result_of<F(Args...)>::type>
{
    using return_type = typename std::result_of<F(Args...)>::type;

    auto task = std::make_shared<std::packaged_task<return_type()>>(
            std::bind(std::forward<F>(f), std::forward<Args>(args)...)
        );

    std::future<return_type> res = task->get_future();

    {
        std::unique_lock<std::mutex> lock(queue_mutex_);

        // 不允许在停止的线程池中加入新的任务
        if(IsStop()){
            //throw std::runtime_error("enqueue on stopped ThreadPool");
            return std::future<return_type>();
        }


        tasks_.emplace([task](){ (*task)(); });
    }

    condition_.notify_one();

    return res;
}


#endif // THREAD_TOOL_H
