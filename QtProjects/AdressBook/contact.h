#ifndef CONTACT_H
#define CONTACT_H

#include<QString>
#include<QDataStream>

struct Contact{
    QString name_;
    QString phone_number_;

    bool operator==(const Contact& other) const{
        return (this->name_ == other.name_) &&(this->phone_number_ == other.phone_number_);
    }
};


QDataStream& operator<<(QDataStream &stream, const Contact& contact){
    return stream << contact.name_ << contact.phone_number_;
}

QDataStream& operator>>(QDataStream &stream, Contact& contact){
    return stream >> contact.name_ >> contact.phone_number_;
}

#endif // CONTACT_H
