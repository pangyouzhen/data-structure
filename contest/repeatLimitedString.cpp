// using std::string;

// int cnt[30];
// class Solution {
// public:
//     int repeatlImitedString(string A, string B) {
//         int n = A.size(), m = B.size();
//         int cnt = 1;
//         string s = A;
//         while (s.size() < m) {
//             s += A;
//             cnt++;
//         }
//         if (s.find(B) != string::npos) return cnt;
//         s += A;
//         cnt++;
//         if (s.find(B) != string::npos) return cnt;
//         return -1;
//     }
// };