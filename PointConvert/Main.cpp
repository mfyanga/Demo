#include<iostream>
#include<chrono>
#include<unistd.h>
#include<random>
#include<fstream>
#include<string>
#include "PointConvert.h"

const int Max_Point_Num = 1000;
const double Min_Point_Data = -100.0;
const double Max_Point_Data = 100.0;


using TMillDuration = std::chrono::duration<double, std::milli>;
using TTimePoint = std::chrono::high_resolution_clock::time_point;

int main(int argc, char **argv)
{
    //std::cout << "Enter main()" << std::endl;
    if (4 != argc)
    {
        std::cout << "invalid input param format" << std::endl;
        std::cout << "Usage:" << std::endl;
        std::cout << argv[0] <<  " x_shift " << " y_shift " << " angle " << std::endl;
        return -1;
    }
    
    //init the relation between coordinate1 and coordinate2
    C2dPoint shift;
    std::string strTmpArg = argv[1];
    shift.SetX(std::stod(strTmpArg));
    strTmpArg = argv[2];
    shift.SetY(std::stod(strTmpArg));  
    strTmpArg = argv[3];
    double rotateAngle = std::stod(strTmpArg); 
    //convert angle to radian
    double rotateRadian = (M_PI / 180) *  rotateAngle;
    
    //create a ofstream for output convert result
    std::ofstream outFile("ConvertResult.txt");
    if (!outFile.is_open())
    {
        std::cout << "open output file faild" << std::endl;
        return -2;
    }
    outFile << "/************************************************************************************************" << std::endl;
    outFile << "Cartesian coordinates XOY to Cartesian coordinates X`O`Y` by move(" \
            << shift.GetX() << " , " << shift.GetY() << ") and rotate " << rotateAngle << " degrees" << std::endl;
    outFile << "*************************************************************************************************/" << std::endl;  

    //generate Max_Point_Num point [-100, 100]
    std::vector<C2dPoint> vecCoordinate1Points;
    /*
    for (int i = 0; i < Max_Point_Num; ++i)
    {   
        //TTimePoint startTimePoint = std::chrono::high_resolution_clock::now();
        auto FRandData = [] (int iMin, int iMax) { return GenAvgRandNumber(iMin, iMax);};
        //double dX = [] (int iMin, int iMax) { return GenAvgRandNumber(iMin, iMax);}(Min_Point_Data, Max_Point_Data);
        C2dPoint tmpPoint;
        double dX = FRandData(Min_Point_Data, Max_Point_Data);
        double dY = FRandData(Min_Point_Data, Max_Point_Data);
        tmpPoint.SetX(dX);
        tmpPoint.SetY(dY);
        vecCoordinate1Points.emplace_back(std::move(tmpPoint));

        //double 
        //std::cout << "dX= " << dX << "\t dY = " << dY << std::endl;
        //usleep(2000 * 1000);
        //TTimePoint endTimePoint = std::chrono::high_resolution_clock::now();
        //TMillDuration millDuration = std::chrono:: duration_cast<TMillDuration>(endTimePoint - startTimePoint);
        //std::cout << "It took me " << millDuration.count() << " mill seconds." << std::endl;
    }
    */
    vecCoordinate1Points.emplace_back(0.0, 0.0);
    vecCoordinate1Points.emplace_back(2.0, 4.0);
    vecCoordinate1Points.emplace_back(3.0, 4.0);
    vecCoordinate1Points.emplace_back(4.0, 5.0);
    vecCoordinate1Points.emplace_back(4.0, 4.0);
    vecCoordinate1Points.emplace_back(7.0, 4.0);
    vecCoordinate1Points.emplace_back(8.0, 3.0);
    vecCoordinate1Points.emplace_back(-2.0, 4.0);
    vecCoordinate1Points.emplace_back(3.0, -4.0);
    vecCoordinate1Points.emplace_back(-4.0, -5.0);
    vecCoordinate1Points.emplace_back(-4.0, 4.0);
    vecCoordinate1Points.emplace_back(-7.0, 4.0);
    vecCoordinate1Points.emplace_back(8.0, -3.0);
    
    //covert coordinate1 points to coordinate2 points
    C2dPoint tmpDestPoint;
    for (auto &point : vecCoordinate1Points)
    {
        TTimePoint startTimePoint = std::chrono::high_resolution_clock::now();   
        PointFromCoord1toCoord2(point, tmpDestPoint, shift, rotateRadian);
        TTimePoint endTimePoint = std::chrono::high_resolution_clock::now();
        TMillDuration millDuration = std::chrono:: duration_cast<TMillDuration>(endTimePoint - startTimePoint);
        outFile << "SrcPoint:(" <<  point.GetX() <<  " , " << point.GetY() << ") to " \
                << "DestPoint(" << tmpDestPoint.GetX() << " , " << tmpDestPoint.GetY() << ")" \
                << " cost " << millDuration.count() << "ms" << std::endl;
     
        
    }
   
    //such code just for some point to check the correctness  
    /* 
    C2dPoint testFromPoint;
    testFromPoint.SetX(0);
    testFromPoint.SetY(0);
    C2dPoint testToPoint;
    PointFromCoord1toCoord2(testFromPoint, testToPoint, shift, rotateRadian);    
    std::cout << "srcPoint(" <<  testFromPoint.GetX() <<  " , " << testFromPoint.GetY() << ") to destPoint(" << testToPoint.GetX() << " , " << testToPoint.GetY() << ")" << std::endl;
    outFile << "srcPoint(" <<  testFromPoint.GetX() <<  " , " << testFromPoint.GetY() << ") to destPoint(" << testToPoint.GetX() << " , " << testToPoint.GetY() << ")" << std::endl;      
    */

    return 0;
}
