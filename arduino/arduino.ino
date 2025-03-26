const int step1 = 2;
const int step2 = 3;
const int dir1 = 5;
const int dir2 = 6;

#define button1 A2
#define button2 A3
#define button3 A1
#define button4 A0
#define EN 8

float targetY = 0;
float targetX = 100;
float currentX = 100;
float currentY = 0;

int m1StepAngle = 0;
int m2StepAngle = 0;

const float L = 100.0;
const float L1 = 90.0;
const float L2 = 150.0;
float correctionFactor(float err1, float err2, float endX, float endY) {
    float distance = sqrt(pow(fabs(endX), 2) + pow(fabs(endY), 2));  // Oblicz odległość do celu
    float maxDistance = fabs(endY - 100);
    return (fabs(err1) + fabs(err2)) * distance / maxDistance;
}


// Poprawienie funkcji m1Angle
float m1Angle(float endX, float endY, float err1, float err2) {  
    float localX = endX;
    float localY = endY;
    
    if (err1 > 0) {
        localY = endY - correctionFactor(err1, err2, endX, endY);
    }

    if (err1 < 0) {
        localY = endY + correctionFactor(err1, err2, endX, endY);
    }
    float distance = sqrt(pow(localY, 2) + pow(localX, 2));
    float cosTheta1 = (pow(L1, 2) + pow(distance, 2) - pow(L2, 2)) / (2 * L1 * distance);
    float theta1 = acos(cosTheta1);
    
    // Upewnij się, że poprawnie obliczasz kąt
    float theta2 = atan2(localY, endX); // Poprawienie argumentów
    return theta2 - theta1;  
}

// Poprawienie funkcji m2Angle
float m2Angle(float endX, float endY, float err1, float err2) {  
    float localX = endX;
    float localY = endY;
    
    // Korekcja w zależności od błędów
    if (err1 < 0) {
        localY = endY + correctionFactor(err1, err2, endX, endY);
    }
    if (err1 > 0) {
        localY = endY - correctionFactor(err1, err2, endX, endY);
    }
    float distance = sqrt(pow(localY, 2) + pow(localX, 2));
    float cosTheta1 = (pow(L1, 2) + pow(distance, 2) - pow(L2, 2)) / (2 * L1 * distance);
    
    float theta1 = acos(cosTheta1);
    float theta2 = atan2(localY, localX); // Poprawienie argumentów
    return theta2 + theta1;
}

int m1Target = m1Angle(targetX, targetY, currentY - targetY, currentX - targetX) / M_PI * 200 * 16;
int m2Target = m1Angle(targetX, targetY, currentY - targetY, currentX - targetX) / M_PI * 200 * 16;

void loop() {
    if (Serial.available() > 0) {
        char incomingByte = Serial.read();
        if (incomingByte != '\r' && incomingByte != '\n') {
            Serial.print("Received: ");
            Serial.println(incomingByte);
            if (incomingByte == 'a') targetX += 1;
            if (incomingByte == 'd') targetX -= 1;
            if (incomingByte == 'w') targetY += 1;
            if (incomingByte == 's') targetY -= 1;
        }

        if (abs(currentX - targetX) > 0.001 || abs(currentY - targetY) > 0.001) {
            m1Target = m1Angle(targetX, targetY, currentY - targetY, currentX - targetX) / M_PI * 200 * 16;
            m2Target = m2Angle(targetX, targetY, currentY - targetY, currentX - targetX) / M_PI * 200 * 16;
            int m1Steps = abs(m1Target - m1StepAngle);
            int m2Steps = abs(m2Target - m2StepAngle);
            int m1Delay = 1000;
            int m2Delay = 1000;

            if (m1Steps > m2Steps) {
                m1Delay = 1000 * m1Steps / max(m1Steps, m2Steps);
                m2Delay = 1000 * m2Steps / max(m1Steps, m2Steps);
            } else if (m2Steps > m1Steps) {
                m2Delay = 1000 * m2Steps / max(m1Steps, m2Steps);
                m1Delay = 1000 * m1Steps / max(m1Steps, m2Steps);
            }

            for (int i = 0; i < m1Steps + m2Steps; i++) {
                if (m1StepAngle < m1Target) {
                    digitalWrite(dir1, HIGH);
                    digitalWrite(step1, HIGH);
                    delayMicroseconds(m1Delay);
                    digitalWrite(step1, LOW);
                    delayMicroseconds(m1Delay);
                    m1StepAngle++;
                } else if (m1StepAngle > m1Target) {
                    digitalWrite(dir1, LOW);
                    digitalWrite(step1, HIGH);
                    delayMicroseconds(m1Delay);
                    digitalWrite(step1, LOW);
                    delayMicroseconds(m1Delay);
                    m1StepAngle--;
                }

                if (m2StepAngle < m2Target) {
                    digitalWrite(dir2, HIGH);
                    digitalWrite(step2, HIGH);
                    delayMicroseconds(m2Delay);
                    digitalWrite(step2, LOW);
                    delayMicroseconds(m2Delay);
                    m2StepAngle++;
                } else if (m2StepAngle > m2Target) {
                    digitalWrite(dir2, LOW);
                    digitalWrite(step2, HIGH);
                    delayMicroseconds(m2Delay);
                    digitalWrite(step2, LOW);
                    delayMicroseconds(m2Delay);
                    m2StepAngle--;
                }
                m1Delay = 50000 / m1Steps;
                m2Delay = 50000 / m2Steps;
                i++;
            }
            currentX = targetX;
            currentY = targetY;
        }
    }
}

void setup() {
    Serial.begin(38400);
    pinMode(step1, OUTPUT);
    pinMode(step2, OUTPUT);
    pinMode(dir1, OUTPUT);
    pinMode(dir2, OUTPUT);
    pinMode(EN, OUTPUT);
    digitalWrite(EN, LOW);
}
