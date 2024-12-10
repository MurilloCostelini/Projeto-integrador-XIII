#include <Stepper.h>

#define STEPS_PER_REV 2048 // Passos para uma volta completa
#define DEGREE_STEPS (STEPS_PER_REV / 360.0) // Passos por grau

Stepper motor1(STEPS_PER_REV, 2, 3, 4, 5);
Stepper motor2(STEPS_PER_REV, 6, 8, 7, 9);
Stepper motor3(STEPS_PER_REV, 10, 11, 12, 13);
Stepper motor4(STEPS_PER_REV, 22, 23, 24, 25);
Stepper motor5(STEPS_PER_REV, 26, 27, 28, 29);

const int MOTOR_SPEED = 10;  // A velocidade do motor tem que mudar aqui 

void realizarMovimento(Stepper &motor, int movimentos) {
  int passosPorMovimento = DEGREE_STEPS * 170;
  for (int i = 0; i < movimentos; i++) {
    motor.step(passosPorMovimento);
    delay(500);
    motor.step(-passosPorMovimento);
    delay(500);
  }
}

void setup() {
  motor1.setSpeed(MOTOR_SPEED);
  motor2.setSpeed(MOTOR_SPEED);
  motor3.setSpeed(MOTOR_SPEED);
  motor4.setSpeed(MOTOR_SPEED);
  motor5.setSpeed(MOTOR_SPEED);

  Serial.begin(9600);
  Serial.println("Pronto para receber comandos.");
}

void loop() {
  if (Serial.available() > 0) {
    String comando = Serial.readStringUntil('\n');
    comando.trim();

    int espaco = comando.indexOf(' ');
    String cor = comando.substring(0, espaco);
    int quantidade = comando.substring(espaco + 1).toInt();

    if (cor == "LARANJA") {
      realizarMovimento(motor1, quantidade);
    } else if (cor == "VERMELHO") {
      realizarMovimento(motor2, quantidade);
    } else if (cor == "AMARELO") {
      realizarMovimento(motor3, quantidade);
    } else if (cor == "AZUL") {
      realizarMovimento(motor4, quantidade);
    } else if (cor == "VERDE") {
      realizarMovimento(motor5, quantidade);
    }

    Serial.println("OK");
  }
}