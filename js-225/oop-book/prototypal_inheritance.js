/*
This exercise re-examines exercise 1 from the previous chapter. In that exercise, you wrote a class to instantiate smartphone objects. In this exercise, we'll rewrite that solution using the constructor/prototype pattern.

Using the constructor/prototype pattern, create a type that represents smartphones. Each smartphone should have a brand, model, and release year. Add methods that display the smartphone's information and check its battery level. Create objects that represent the following two smartphones:

Brand	Model	Release Year
Apple	iPhone 12	2020
Samsung	Galaxy S21	2021
*/

function SmartPhone(brand, model, releaseYear) {
  this.brand = brand;
  this.model = model;
  this.releaseYear = releaseYear;
  this.batteryLevel = 100;
}

SmartPhone.prototype.checkBatteryLevel = function() {
  console.log(this.batteryLevel);
}

SmartPhone.prototype.displayInfo = function() {
  console.log(`${this.brand} ${this.model} - Released ${this.releaseYear}`);
}

let iPhone12 = new SmartPhone('Apple', 'iPhone 12', 2020);
let galaxy = new SmartPhone('Samsung', 'Galaxy S21', 2021);

iPhone12.checkBatteryLevel();
iPhone12.displayInfo();

galaxy.checkBatteryLevel();
galaxy.displayInfo();


/*
This exercise re-examines exercise 3 from the previous chapter. In that exercise, you wrote a class hierarchy to represent vehicles of various types. In this exercise, we'll rewrite that solution using the constructor/prototype pattern.

Using the constructor/prototype pattern, create some types that represent vehicles, including cars, boats, and planes as specific kinds of vehicles. All vehicles should be able to accelerate and decelerate. Cars should be able to honk, boats should be able to drop anchor, and planes should be able to take off and land. Test your code.
*/

function Vehicle(color, weight) {
  this.color = color;
  this.weight = weight;
}

Vehicle.prototype.accelerate = function() {
  console.log('Accelerating...');
}

Vehicle.prototype.decelerate = function() {
  console.log('Decelerating...');
}



function Car(color, weight, licenseNumber) {
  Vehicle.call(this, color, weight);
  this.licenseNumber = licenseNumber;
}

Car.prototype = Object.create(Vehicle.prototype);
Car.prototype.constructor = Car;
Car.prototype.honk = function() {
  console.log('Honk!');
}



function Boat(color, weight, homePort) {
  Vehicle.call(this, color, weight);
  this.homePort = homePort;
}

Boat.prototype = Object.create(Vehicle.prototype);
Boat.prototype.constructor = Boat;
Boat.prototype.dropAnchor = function() {
  console.log('Dropping an anchor.');
}



function Plane(color, weight, airline) {
  Vehicle.call(this, color, weight);
  this.airline = airline;
}

Plane.prototype = Object.create(Vehicle.prototype);
Plane.prototype.constructor = Plane;
Plane.prototype.takeOff = function() {
  console.log('Taking off!');
}
Plane.prototype.land = function() {
  console.log('Landing!');
}