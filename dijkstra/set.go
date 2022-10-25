package main

import "fmt"

func makeSet() *Set {
	return &Set{
		keys: make(map[int]struct{}),
	}
}

type Set struct {
	keys map[int]struct{}
}

func (s *Set) Add(k int) {
	s.keys[k] = struct{}{}
}

func (s *Set) Has(k int) bool {
	_, has := s.keys[k]
	return has
}

func (s *Set) Del(k int) error {
	has := s.Has(k)
	if !has {
		return fmt.Errorf("item does not exist")
	}
	delete(s.keys, k)
	return nil
}

func (s *Set) Len() int {
	return len(s.keys)
}

func (s *Set) Iter() chan int {
	c := make(chan int)
	go func() {
		for k := range s.keys {
			c <- k
		}
		close(c)
	}()
	return c
}
