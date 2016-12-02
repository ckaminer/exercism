class Bob {
  def hey(greeting: String) : String = greeting match {
    case greeting if (greeting.takeRight(1) == "?") => "Sure."
    case greeting if (greeting.takeRight(1) == "!") => "Whoa, chill out!"
    case "" => "Fine. Be that way!"
    case _ => "Whatever."
  }
}
