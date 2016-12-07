object SumOfMultiples {
  def sumOfMultiples(denoms: List[Int], num: Int): Int = {
    var matches = Array[Int]();

    for(a <- 1 to (num - 1)){
      for (denom <- denoms) {
        if (a % denom == 0) {
          matches = matches :+ a
        }
      }
    }
    matches.distinct.sum
  }
}
