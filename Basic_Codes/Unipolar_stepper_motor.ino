const int stepPin = 5; 
const int dirPin = 4; 
 
void setup() 
{
  // Sets the two pins as Outputs
  pinMode(stepPin,OUTPUT); 
  pinMode(dirPin,OUTPUT);
}

void loop() 
{
  digitalWrite(dirPin,HIGH); // Enables the motor to move in a particular direction
  // Makes 200 pulses for making one full cycle rotation
  for(int x = 0; x < 1000; x++) {
    digitalWrite(stepPin,HIGH); 
    delayMicroseconds(1500); 
    digitalWrite(stepPin,LOW); 
    delayMicroseconds(1500); 
  }
  delay(500); // One second delay
  
  digitalWrite(dirPin,LOW); //Changes the rotations direction
  // Makes 400 pulses for making two full cycle rotation
  for(int x = 0; x < 1000; x++) {
    digitalWrite(stepPin,HIGH);
    delayMicroseconds(1500);
    digitalWrite(stepPin,LOW);
    delayMicroseconds(1500);
  }
  delay(500);
}
