#include <Servo.h>
Servo myservo15;
Servo myservo13;
Servo myservo12;
Servo myservo14;
Servo myservo2;
Servo myservo0;
Servo myservo4;
Servo myservo5;
Servo myservo16;
Servo myservo10;

void setup()
{
  myservo15.attach(15);
  myservo13.attach(13);
  myservo12.attach(12);
  myservo14.attach(14);
  myservo2.attach(2);
  myservo0.attach(0);
  myservo4.attach(4);
  myservo5.attach(5);
  myservo16.attach(16);
  myservo10.attach(10);

  Serial.begin(115200);
  Serial.println("Starts");
}

void loop()
{
  int q[11]={5,1,3,15,13,12,14,2,0,4};

    if (Serial.available()>0)
    {
      String temp = Serial.readStringUntil('$');
      Serial.println(temp);
      int a = temp.charAt(0);
      int b = temp.substring(2,6).toInt();
      //Serial.println(q[a-48]);
      switch (q[a-48])
      {
      case 1:
      myservo15.write(b);
      Serial.println("first servo");
      break;

      case 3:
      myservo13.write(b);
      Serial.println("seconf servo");
      break;

      case 15:
      myservo12.write(b);
      Serial.println("third servo");
      break;

      case 13:
      myservo14.write(b);
      Serial.println("fourth servo");
      break;

      case 12:
      myservo2.write(b);
      Serial.println("fifth servo");
      break;

      case 14:
      myservo0.write(b);
      Serial.println("sixth servo");
      break;

      case 2:
      myservo4.write(b);
      Serial.println("7th servo");
      break;

      case 0:
      myservo5.write(b);
      Serial.println("8th servo");
      break;

      case 4:
      myservo16.write(b);
      Serial.println("9th servo");
      break;

      case 5:
      myservo10.write(b);
      Serial.println("10th servo");
      break;

      
    }
  }
}

