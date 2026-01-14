class Solution {
    func numRescueBoats(_ people: [Int], _ limit: Int) -> Int {
        let arr = people.sorted()

        var heavyP = arr.count - 1 
        var lightP = 0
        var boatNum = 0

        while (lightP <= heavyP) {
            if (arr[lightP] + arr[heavyP] <= limit) {
                boatNum += 1
                lightP += 1
                heavyP -= 1
            } else {
                boatNum += 1
                heavyP -= 1
            }
        }

        return boatNum
    }
}