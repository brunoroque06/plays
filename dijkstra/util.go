package main

func If[T any](cond bool, vt, vf T) T {
	if cond {
		return vt
	}
	return vf
}

func Map[T any, V any](l []T, f func(T) V) []V {
	res := make([]V, len(l))
	for i, v := range l {
		res[i] = f(v)
	}
	return res
}
