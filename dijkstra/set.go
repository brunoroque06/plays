package main

import "fmt"

func MakeSet[T comparable]() *Set[T] {
	return &Set[T]{
		keys: make(map[T]struct{}),
	}
}

type Set[T comparable] struct {
	keys map[T]struct{}
}

func (s *Set[T]) Add(k T) {
	s.keys[k] = struct{}{}
}

func (s *Set[T]) Has(k T) bool {
	_, ok := s.keys[k]
	return ok
}

func (s *Set[T]) Del(k T) error {
	has := s.Has(k)
	if !has {
		return fmt.Errorf("item does not exist")
	}
	delete(s.keys, k)
	return nil
}

func (s *Set[T]) Len() int {
	return len(s.keys)
}

func (s *Set[T]) Iter() chan T {
	c := make(chan T)
	go func() {
		for k := range s.keys {
			c <- k
		}
		close(c)
	}()
	return c
}
