/*
 * Smart Sprinkler using an Arduino Uno.
 *
 * This code simply measures the moisture in the soil and the
 * brightness. It accepts the following commands to access data or change
 * the sprinkler to be on or off:
 *
 *      read light
 *      read moisture
 *      read status
 *      write on
 *      write off
 */
#include <LiquidCrystal.h>
#include <Servo.h>

// #define DEBUG
#define MOISTURE_PIN    0       /* Analog pin for the moisture sensor */
#define LIGHT_PIN       2       /* Analog pin for the photo sensor */
#define SERVO_PIN       A1      /* Analog pin for servo */
#define LED_PIN         7       /* Digital pin to control the sprinkler */
#define SLEEP_INTERVAL  10      /* ms */

boolean sprinkler_status;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
Servo servo;

void setup() {
    /* Start serial communication at 115200 Hz */
    Serial.begin(115200);
    while(!Serial);
    Serial.setTimeout(10);

    /*
     * Sensor should be on an analog pin which does not require calling
     * pinMode; LED is digital.
     */
    sprinkler_status = false;
    pinMode(LED_PIN, OUTPUT);

    /* Start LCD */
    lcd.begin(16, 2);

    lcd.setCursor(0, 1);
    lcd.print("Status: OFF");

    /* Attach servo */
    servo.attach(SERVO_PIN);
}
void loop() {
    char *moisture, *light;
    /* Read sensor */
    int moisture_data = analogRead(MOISTURE_PIN);
    int light_data = analogRead(LIGHT_PIN);

    /* Convert to human readable format */
    if (moisture_data == 0) {
        moisture = "AIR";
    }
    else if (moisture_data < 300) {
        moisture = "DRY";
    }
    else if (moisture_data < 700) {
        moisture = "HUMID";
    }
    else {
        moisture = "WET";
    }

    if (light_data < 650) {
        light = "DIM";
    }
    else {
        light = "BRIGHT";
    }

#ifdef DEBUG
    /* Output data to Serial */
    Serial.print(moisture_data);
    Serial.print("   (");
    Serial.print(moisture);
    Serial.print(")   ");
    Serial.print(light_data);
    Serial.print("   (");
    Serial.print(light);
    Serial.print(")     \r");
#endif /* DEBUG */
    /* and to LCD */
    lcd.setCursor(0, 0);
    lcd.print(moisture);
    lcd.print("/");
    lcd.print(light);
    lcd.print("                ");

    /* Check if there's data for reading */
    if (Serial.available()) {
        /*
         * Can receive the following:
         *  "read light"
         *  "read moisture"
         *  "read status"
         *  "write on"
         *  "write off"
         * NOTE: each command will end in '\r\n'
         */
        String msg = Serial.readString();
#ifdef DEBUG
        Serial.print("Got: ");
        Serial.println(msg);
#endif /* DEBUG */

        if (msg.startsWith("read ")) {
            String query = msg.substring(5);
            /* for (int i = 0; i < query.length(); i++) { */
            /*     Serial.print((int)query.charAt(i)); */
            /*     Serial.print(" "); */
            /* } */
            if (query == "light\r\n") {
                Serial.println(light);
            }
            else if (query == "moisture\r\n") {
                Serial.println(moisture);
            }
            else if (query == "status\r\n") {
                Serial.println(sprinkler_status ? "ON" : "OFF");
            }
        }
        else if (msg.startsWith("write ")) {
            String query = msg.substring(6);
            lcd.setCursor(0, 1);
            if (query == "on\r\n") {
                sprinkler_status = true;
                digitalWrite(LED_PIN, HIGH);
                lcd.print("Status: ON ");
                servo.write(0);     // 0 degress
            }
            else if (query == "off\r\n") {
                sprinkler_status = false;
                digitalWrite(LED_PIN, LOW);
                lcd.print("Status: OFF");
                servo.write(90);    // 90 degress
            }
        }
    }

    /* Sleep */
    delay(SLEEP_INTERVAL);
}
