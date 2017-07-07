package clock

import (
  "fmt"
)

const testVersion = 4

type Clock struct {
    hour int
    minute int
}

func New(hour, minute int) Clock {
  returnMinute := minute % 60
  if returnMinute < 0 {
    returnMinute += 60
    hour--
  }
  returnHour := (hour + minute/60) % 24
  if returnHour < 0 {
    returnHour += 24
  }
  return Clock{hour: returnHour, minute: returnMinute}
}

func (c *Clock) String() string {
  return fmt.Sprintf("%02d:%02d", c.hour, c.minute)
}

func (c Clock) Add(minutes int) Clock {
  return New(c.hour, c.minute + minutes)
}
