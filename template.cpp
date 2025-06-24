#include <bits/stdc++.h>
using namespace std;

// Typedefs for convenience
#define ll long long
#define pii pair<ll, ll>
#define vll vector<ll>
#define vpii vector<pii>
#define pb push_back
#define F first
#define S second

// Fast IO
#define fast() ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

// Common loops
#define loop(i,a,b) for(ll i = a; i < b; i++)
#define rev(i,a,b) for(ll i = b-1; i >= a; i--)
#define rep(i,n) for(ll i = 0; i < n; i++)

// Utils
#define all(x) x.begin(), x.end()
#define sorta(a,n) sort(a, a+n)
#define sortv(v) sort(all(v))
#define mp make_pair

// Constants
const ll MOD = 1e9 + 7;
const ll INF = 1e18;

// Short helper functions
ll gcd(ll a, ll b) { return b ? gcd(b, a % b) : a; }
ll lcm(ll a, ll b) { return (a / gcd(a, b)) * b; }

ll maxSubArray(vector<ll>& v) {
    ll cur = 0, mx = -INF;
    for (auto x : v) {
        cur = max(x, cur + x);
        mx = max(mx, cur);
    }
    return mx;
}

string decToBin(ll n) {
    string s = "";
    while (n) s = char(n % 2 + '0') + s, n /= 2;
    return s.empty() ? "0" : s;
}

void solve() {

}

int main() {
    fast();
    ll t = 1;
    cin >> t;
    while (t--) solve();
    return 0;
}
