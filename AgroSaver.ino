#define BUZZER_PIN 7  // Connect the S (signal) pin here

void setup() {
  Serial.begin(9600); // Initialize serial communication
  pinMode(BUZZER_PIN, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    data.trim();

    if (data == "rat") {
      ratBeep();
    } 
    else if (data == "snake") {
      snakeBeep();
    } 
    else {
      noBeep(); // Ensure no sound if no detection
    }
  }
}

void ratBeep() {
  digitalWrite(BUZZER_PIN, HIGH); // Loud beep for 1 second
  delay(1000);
  digitalWrite(BUZZER_PIN, LOW);
}

void snakeBeep() {
  for (int i = 0; i < 2; i++) {
    digitalWrite(BUZZER_PIN, HIGH); // Beep for 0.5 second
    delay(500);
    digitalWrite(BUZZER_PIN, LOW);
    delay(500); // Pause between beeps
  }
}

void noBeep() {
  digitalWrite(BUZZER_PIN, LOW); // Ensure buzzer is off
}
