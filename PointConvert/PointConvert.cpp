#include<cmath>
#include<random>
#include<functional>
#include<iostream>
#include"PointConvert.h"
//used to compare double data with zero
const double PRECISION = 0.000001;

double GenAvgRandNumber(double dMin, double dMax)
{
   std::random_device rd;
   std::mt19937 gen(rd());
   std::uniform_real_distribution<double> dis(dMin, dMax);
   return dis(gen);
}

void PointFromCoord1toCoord2(const C2dPoint  &from, C2dPoint &to, const C2dPoint  &coodiateShift, double radian)
{
    //coordinate move vector
    const double dShiftX = coodiateShift.GetX();
    const double dShiftY = coodiateShift.GetY();
    
    //point in coordinate1
    const double dFromX = from.GetX();
    const double dFromY = from.GetY();

    //step one:convert coodinate move to point move
    //std::function<void(int x)> 
    double dShift = [dShiftX] (int iDirection) ->  double { return (double)(iDirection * dShiftX); } (-1);
    //std::cout << "point.x move " << dShift << std::endl;
    double tmpX = dFromX + dShift;
    dShift = [dShiftY] (int iDirection) { return (double)(iDirection * dShiftY); } (-1);
    //std::cout << "point.x move " << dShift << std::endl;
    double tmpY = dFromY + dShift;

    //step two:convert coordinate rotate to point rotate
    //after step one , assuming that A is the point radian ，get sin(A), cos(A)
    double dR = sqrt(tmpX * tmpX + tmpY * tmpY);
    //if the point is the Origin of the coordinates after step one
    //auto  FLambadaSetPoint = [ &to ] (double x, double y) { to.SetX(x); to.SetY(y); };
    std::function<void (double, double)> FLambadaSetPoint = [ &to ] (double x, double y) { to.SetX(x); to.SetY(y); };
    if (dR < PRECISION)
    {
        FLambadaSetPoint(0, 0);
        return ;
    }
    
    double dSinA = tmpY / dR;
    double dCosA = tmpX / dR;

    //the point after rotate
    //abscissa dPrimeX = dR * cos(A + rotateRadian)
    //ordinate dPrimeY = dR * sin(A + rotateRadian)
    double rotateRadian  = [radian] (int iDirection) { return (double)(iDirection * radian); } (-1);
    double dCosRotateRadian = cos(rotateRadian);
    double dSinRotateRadian = sin(rotateRadian);
    double dPrimeX = dR * (dCosA * dCosRotateRadian - dSinA * dSinRotateRadian);
    double dPrimeY = dR * (dSinA * dCosRotateRadian  + dCosA * dSinRotateRadian);
    if (fabs(dPrimeX) < PRECISION)
    {
        dPrimeX = 0;
    }
    if (fabs(dPrimeY) < PRECISION)
    {
        dPrimeY = 0;
    }
    FLambadaSetPoint(dPrimeX, dPrimeY);
  
    return;
}
