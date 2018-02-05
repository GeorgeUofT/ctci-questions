# Find the smallest difference between any two elements of two arrays.

# Of course an O(n*lg(n) + m*lg(n)) solutions exists in which we only sort
# one array and search through it for the closest to each element of the other,
# but this O(n*lg(n) + m*lg(m)) solution feels more simple.
# And, sometimes at least, simplicity counts for something.

# Also, there is an O(d*n + m) solution where d is the smallest difference
# found between a constant number of terms at the beginning of the two arrays.
# This solution would continue by storing d items in a hash table for each
# element in the first array.

