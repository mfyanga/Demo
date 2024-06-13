#include <QCoreApplication>
#include <QDebug>
#include <iostream>
#include <future>
#include <string>
#include <chrono>
#include <vector>
#include <thread>

#include "thread_tool.h"

int PrintS(const std::string& level, std::string &str){
    std::string origin_str = "origin: ";
    origin_str += str;
    QString qorigin_str = QString::fromStdString(origin_str);
    qDebug() << qorigin_str;

    str = level + "_" + str;
    QString qstr = QString::fromStdString(str);
//    std::this_thread::sleep_for(std::chrono::seconds(10));
//    qDebug() << qstr;

    return 0;
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    qDebug() << "Begin test std::future";

//    std::future<int> futre_result = std::async(Print, "hello");
//    std::vector<std::future<int>> result_set;
//    result_set.emplace_back(std::async(Print, "hello"));
//    result_set.push_back(std::async(Print, "hello"));
    //result_set.emplace_back(std::move(futre_result));

//    std::chrono::milliseconds timeout(100);
//    std::future_status status = futre_result.wait_for(timeout);

//    if (std::future_status::ready == status) {
//       qDebug() << "Wait the result of task successfully.";
//    } else if (std::future_status::timeout == status){
//      qDebug() << "Wait the result of task timeout.";
//    }else {
//      qDebug() << "Wait other result.";
//    }
//    futre_result.get();

    const std::size_t max_num = 100;
    std::vector<std::string> msgs;
    for (std::size_t i = 0; i < max_num; ++i){
        msgs.push_back(std::to_string(i));
    }
    const auto numCores = std::thread::hardware_concurrency();
    qDebug() << numCores;

    ThreadPool thread_pool(numCores);

    for (std::size_t j = 0; j < 10; ++j) {
        std::string l = std::string("j_") + std::to_string(j);

        std::vector<std::future<int>> results;
        for (auto& msg : msgs){
            results.emplace_back(thread_pool.enqueue(PrintS, l, msg));
            qDebug() << QString::fromStdString(msg);
        }

        for (auto& result : results) {
            result.get();
        }

        std::string str_j = "j_";
        str_j += std::to_string(j);
        QString qstr_j =  QString::fromStdString(str_j);
        qDebug() << qstr_j;
    }



    qDebug() << "End test std::future";

    return a.exec();
}
