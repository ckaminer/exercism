module BookKeeping
  VERSION = 3
end

class Hamming
  def self.compute(first, second)
    self.error_check(first,second)
    counter = 0
    first.chars.each_with_index do |char, index|
      counter += 1 if first[index] != second[index]
    end
    counter
  end

  def self.error_check(first, second)
    if first.length != second.length
      raise ArgumentError
    end
  end
end
