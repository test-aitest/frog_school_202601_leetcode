function numRescueBoats(people: number[], limit: number): number {
  people.sort();

  var heavyP = people.length - 1;
  var lightP = 0;
  var boatNum = 0;

  while (lightP <= heavyP) {
    if (people[lightP] + people[heavyP] <= limit) {
      boatNum++;
      lightP++;
      heavyP--;
    } else {
      boatNum++;
      heavyP--;
    }
  }

  return boatNum;
}
