#include <iostream>
#include <vector>
#include <cstdlib>

int count_non_zeros(std::vector<int> &a) {
  int count = 0;
  for (int i : a) {
    if (i != 0)
      count++;
  }
  return count;
}

void print_result(std::vector<int> &a, int n) {
  int k = 0;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j)
      std::cout << a[k++] << " ";
    std::cout << "\n";
  }
}

bool is_valid(std::vector<int> &a, int n) {
  if (a.back() != 0) {
    int i = a.size() - 1;
    bool left = i % n == 0;
    bool right = i % n == n - 1;
    bool above = i >= n;
    if (!left) {
      if (a[i - 1] != 0 && a[i] != a[i - 1]) return false;
      if (above && a[i - n - 1] == 1 && a[i] == 1) return false;
    }
    if (above) {
      if (a[i - n] != 0 && a[i] != a[i - n]) return false;
      if (!right && a[i - n + 1] == 2 && a[i] == 2) return false;
    }
  }
  return true;
}

void solve(std::vector<int> &a, const int n, const int d) {
  if (a.size() == n * n) {
    if (count_non_zeros(a) == d) {
      print_result(a, n);
      std::cout << "\n";
    }
    return;
  }
  int values[3] = {1, 2, 0};
  for (int val : values) {
    a.push_back(val);
    if (is_valid(a, n))
      solve(a, n, d);
    a.pop_back();
  }
}

int main(const int argc, char** argv) {
  int n = atoi(argv[1]);
  int d = atoi(argv[2]);
  std::vector<int> a;
  a.reserve(n * n);
  solve(a, n, d);
  return 0;
}