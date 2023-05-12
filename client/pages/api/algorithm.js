//path: client/pages/api/algorithm.js

export default function algorithm(
  temperature,
  humidity,
  windChill
) {
  let clothingItems = [];

  if (temperature > 80) {
    clothingItems.push("shorts", "t-shirt", "sun hat");
  } else if (temperature > 60) {
    clothingItems.push("shorts", "long-sleeved shirt", "sun hat");
  } else if (temperature > 40) {
    clothingItems.push("long pants", "sweater or fleece", "beanie");
  } else if (temperature > 20) {
    clothingItems.push(
      "heavy coat",
      "insulated pants",
      "warm gloves",
      "beanie"
    );
  } else {
    clothingItems.push(
      "arctic-rated coat",
      "insulated boots",
      "warm hat",
      "gloves"
    );
  }

  if (humidity > 60) {
    clothingItems.push("moisture-wicking shirt", "moisture-wicking underwear");
  }

  if (windChill < 0) {
    clothingItems.push("face mask", "neck gaiter", "warm socks");
  }

  return clothingItems;
}
