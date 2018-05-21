#ifndef _POINT_CONVERT_H_
#define _POINT_CONVERT_H_

//defien the coordinate point struct
class C2dPoint
{

public:
    explicit C2dPoint() : m_dX(0.0), m_dY(0.0)
    {
    }
    
    explicit C2dPoint(double x, double y)
    {
        m_dX = x;
        m_dY = y;
    } 
public:
    double GetX() const
    {
        return m_dX;
    }

    double GetY() const
    {
        return m_dY;
    }

    void SetX(double x)
    {
        m_dX = x;
    }

    void SetY(double y)
    {
        m_dY = y;
    }

private:
   double m_dX;
   double m_dY;
};

//genearate random data in [Min, Max]
double GenAvgRandNumber(double dMin, double dMax);

//convrt point from Cartesian coordinate XOY to Cartesian coordinate X`O`Y`
void PointFromCoord1toCoord2(const C2dPoint  &from, C2dPoint  &to, const C2dPoint &coodiateShift, double radian);
#endif
