package main

import "sort"

func numRescueBoats(people []int, limit int) int {
	sort.Ints(people)

	heavyP := len(people) - 1
	lightP := 0
	boatNum := 0

	for lightP <= heavyP {
		if people[lightP]+people[heavyP] <= limit {
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
