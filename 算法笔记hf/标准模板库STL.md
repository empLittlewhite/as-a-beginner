
# vector

```cpp
# vector的用法
# push_back
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v;
    int n,x;
    cin >> n;
    for (int i = 0;i<=n-1;i++){
        cin >> x;
        v.push_back(x);
    }
    for(int i =0;i<=v.size()-1;i++){
        if(i != v.size()-1){
            cout<< v[i] << " ";
        }else{
            cout << v[i];
        }
    }
    return 0;
}


# 初始化vector
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n,k;
    cin >> n >> k;
    vector<int> v(n,k);
    for(int i =0; i<=v.size()-1 ;i++){
        if (i != v.size()-1){
            cout << v[i] << " ";
        }else{
            cout << v[i];
        }
    }

    return 0;
}


#初始化+pop_back
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n,k;
    cin >> n >> k;
    vector<int> v(n,0);
    for(int i=1;i <= k ; i++){
        v.pop_back();
    }
    cout << v.size();
    return 0;
}
# clear()
int main() {
    int n;
    cin >> n;
    vector<int> v(n,0);
    v.clear();
    cout<< v.size();

    return 0;
}

#erase
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n,a,x,k1,k2;
    cin >> n;
    vector<int> v;
    for(int i = 0;i <= n-1 ;i++){
        cin >> a;
        v.push_back(a);
    }
    cin >> x >> k1 >> k2;
    v.insert(v.begin() + k1,x);
    v.erase(v.begin() + k2);
    for(int i =0; i <= v.size()-1;i++){
        if (i != v.size()-1){
            cout << v[i] << " ";
        }else{
            cout << v[i];
        }
    }
    return 0;
}

# 比较大小
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n,m,x;
    cin >> n >> m;
    vector<int> v1,v2;
    for(int i = 0; i <= n-1;i++){
        // 这个x可以多次利用的
        cin >> x;
        v1.push_back(x);
    }
    for(int i = 0; i <= m-1;i++){
        // 这个x可以多次利用的
        cin >> x;
        v2.push_back(x);
    }
    if (v1 < v2){
        cout << "Yes";
    }else{
        cout << "No";
    }
    return 0;
}


# 二维数组
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> vs[10];
    int n,x,k;
    cin >> n;
    for(int i=0; i < n ;i++ ){
        cin >> k;
        for(int j=0; j < k;j++ ){
            cin >> x;
            vs[i].push_back(x);
        }
    }

    for(int i=0; i <= n ; i++){
        for(int j=0; j < vs[i].size();j++){
            if(j != vs[i].size()-1){
                cout << vs[i][j] << " ";
            }else{
                cout << vs[i][j];
            }
        }
        cout << endl;
    }
    return 0;
}


```

# set

```cpp
# set和iterator

#include <iostream>
#include <set>
using namespace std;

int main() {
    set<int> s;
    int n,x;
    cin >> n;
    for(int i=0; i<= n-1;i++){
        cin >> x;
        s.insert(x);
    }
    set<int>::iterator it;
    for(it = s.begin(); it != s.end(); it++){
        if(it != s.end()){
            cout << *it << " ";
        }else{
            cout << *it;
        }
    }
    return 0;
}


# 奇葩输出、
#include <iostream>
#include <set>
using namespace std;

int main() {
    set<int> s;
    int n,x;
    cin >> n;
    for(int i=0; i<= n-1;i++){
        cin >> x;
        s.insert(x);
    }
    set<int>::iterator it;
    for(it = s.begin(); it != s.end(); it++){
        if(it != s.begin()){
            cout << " " ;
        }
        cout << *it ;
    }
    return 0;
}


#erase 删除判断，是否是尾指针
#include <iostream>
#include <set>
using namespace std;

int main() {
    int n,x,a;
    set<int> s;
    cin >> n >>x;
    for(int i = 0; i <= n-1;i++){
        cin >> a;
        s.insert(a);
    }
    set<int>::iterator it = s.find(x);
    if(it != s.end()){
        s.erase(it);
    }
    for(it = s.begin();it != s.end();it++){
        if(it != s.begin()){
            cout << " ";
        }
        cout << *it;
    }
    return 0;
}

# erase 的另一个用法

#include <iostream>
#include <set>
using namespace std;

int main() {
    set<int> s;
    int n,x,a;
    cin >> n >> x;
    // 遵循程序员的左闭右开
    for(int i = 0; i< n; i++){
        cin >> a;
        s.insert(a);
    }
    s.erase(x);
    for(set<int>::iterator it = s.begin();it != s.end();it++){
        if(it != s.begin()){
            cout << " ";
        }
        cout << *it;
    }
    return 0;
}

# clear()
int main() {
    set<int> s;
    int n,a;
    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> a;
        s.insert(a);
    }
    s.clear();
    cout << s.size();
    return 0;
}

```

# string

```cpp
# 输入输出

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;
    cout << s;

    return 0;
}

int main() {
    string s;
    getline(cin,s);
    cout << s;
    return 0;
}

#字符串拼接

int main() {
    string s1,s2;
    cin >> s1 >> s2;
    string s3 = s1 + s2;
    cout << s3;
    return 0;
}

# 字符串比较

int main() {
    string s1, s2;
    cin >> s1 >> s2;
    if(s1 > s2){
        cout << "1";
    }else if(s1 < s2){
        cout << "-1";
    }else{
        cout << "0";
    }
    return 0;
}

# clear()和length()
int main() {
    string s;
    cin >> s;
    cout << s.length() << " ";
    s.clear();
    cout << s.length();
    
    return 0;
}

# insert() 和 erase()
int main() {
    string s;
    cin >> s;
    int k1,k2;
    char c;
    cin >> k1 >> c >> k2;
    s.insert(s.begin() + k1,c);
    s.erase(s.begin() + k2);
    cout << s;
    return 0;
}

# substr
int main() {
    string s;
    cin >> s;
    int k,len;
    cin >> k >> len;
    cout << s.substr(k,len);
    return 0;
}
#find substr
int main() {
    string s1,s2;
    cin >> s1 >> s2;
    if(s1.find(s2) != string::npos){
        cout << s1.find(s2) ;
    }else{
        cout << "-1";
    }
    return 0;
}

# replace

int main() {
    string s1,s2;
    cin >> s1;
    int k,len;
    cin >> k >> len >> s2;
    s1.replace(k,len,s2);
    cout << s1;
    return 0;
}

``` 





# map

```cpp

# 赋值   遍历
int main() {
    map<char,int> mp;
    int n;
    cin >> n;
    char key;
    int val;
    for(int i = 0; i < n;i++){
        cin >> key >> val;
        mp[key] = val;
    }
    for(map<char,int>::iterator it = mp.begin();it != mp.end();it++){
        cout << it -> first << " "<< it -> second << endl;
    }
    return 0;
}


# find
int main() {
    map<char,int> mp;
    int n;
    cin >> n;
    char key;
    int val;
    for(int i = 0;i < n;i++){
        cin >> key >> val;
        mp[key] = val;
    }
    cin >> key;
    map<char,int>::iterator it = mp.find(key);
    if(it != mp.end()){
        cout << it ->second;
    }else{
        cout << "-1";
    }
    return 0;
}


# erase()
int main() {
    map<char,int> mp;
    int n;
    cin >> n;
    char key;
    int val;
    for(int i = 0; i < n;i++){
        cin >> key >> val;
        mp[key] = val;
    }
    cin >> key;
    mp.erase(key);
    for(map<char,int>::iterator it = mp.begin(); it != mp.end();it++){
        cout << it ->first << " "<< it -> second << endl; 
    }
    return 0;
}

# clear()  和  size()
int main() {
    map<char,int> mp;
    int n;
    cin >> n;
    char key;
    int val;
    for(int i = 0; i < n;i++){
        cin >> key >> val;
        mp[key] = val;
    }
    cout << mp.size() << " ";
    mp.clear();
    cout << mp.size();
    return 0;
}

# 访问与操作

#include <iostream>
#include <map>
using namespace std;

int main() {
    map<char,int> mp;
    int n;
    cin >> n;
    char key;
    int val;
    for(int i = 0; i < n;i++){
        cin >> key >> val;
        mp[key] = val;
    }
    for(map<char,int>::iterator it = mp.begin();it != mp.end();it++){
        cout << it -> first << " "<< it -> second << endl;
    }
    return 0;
}


```


# queue

```cpp
#push


#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> q;
    int n,a;
    cin >> n;
    for(int i=0;i < n;i++){
        cin >> a;
        q.push(a);
    }
    cout << q.front() << " ";
    cout << q.back();


    return 0;
}




# empty

#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> q;
    int n,k,a;
    cin >> n >> k;
    for(int i = 0; i <n; i++){
        cin >> a;
        q.push(a);
    }
    for(int i = 0; i < k; i++){
            q.pop();
    }
    if(q.empty() != true){
    cout << q.front() << " " << q.back();
    }else{
        cout << "empty queue";
    }
    return 0;
}


# size()

int main() {
    queue<int> q;
    int n,k,a;
    cin >> n >> k;
    for(int i = 0; i < n ;i++){
        cin >> a;
        q.push(a);
    }
    for(int i = 0; i < k; i++){
            q.pop();
    }
    cout << q.size();
    return 0;
}

```

# priority_queue

```cpp

#push()   pop()
#include <iostream>
#include <queue>
using namespace std;

int main() {
    priority_queue<int> q;
    int n,a;
    cin >> n ;
    for(int i = 0; i <n; i++){
        cin >> a;
        q.push(a);
    }
    cout << q.top();
    return 0;
}


# pop() empty()
#include <iostream>
#include <queue>
using namespace std;

int main() {
    priority_queue<int> q;
    int n,k,a;
    cin >> n >> k;
    for(int i = 0; i < n ;i++){
        cin >> a;
        q.push(a);
    }
    for(int i = 0; i < k; i++){
            q.pop();
    }
    if (q.empty() != true){
        cout << q.top() ;
    }else{
        cout << "empty priority queue";
    }
    return 0;
}

#size()
int main() {
    priority_queue<int> q;
    int n,k,a;
    cin >> n >> k;
    for(int i = 0; i < n ;i++){
        cin >> a;
        q.push(a);
    }
    for(int i = 0; i < k; i++){
            q.pop();
    }
    cout << q.size();
    return 0;
}



# 优先级
int main() {
    priority_queue<int,vector<int>,greater<int> > q;
    int n,a;
    cin >> n;
    for(int i = 0; i < n ;i++){
        cin >> a;
        q.push(a);
    }
    cout << q.top();
    return 0;
}

#结构体

#include <iostream>
#include <queue>
#include <string>
using namespace std;

struct Fruit{
    string name;
    int price;
    friend bool operator < (Fruit f1, Fruit f2){
        return f1.price > f2.price;
    }
};
int main() {
    priority_queue<Fruit > q;
    int n;
    string name;
    int price;
    cin >> n;
    for(int i = 0; i < n ;i++){
        cin >> name >> price;
        Fruit f;
        f.name = name;
        f.price = price;
        q.push(f);
    }
    cout << q.top().name << " " << q.top().price;
    return 0;
}

```


# stack

```cpp


#push\top
#include <iostream>
#include <stack>
using namespace std;

int main(){
    stack<int> s;
    int n,a;
    cin >> n;
    for (int i = 0; i < n ; i++){
        cin >> a;
        s.push(a);
    }
    cout << s.top();
    return 0;
}

# pop()

int main(){
    stack<int> s;
    int n,a,k;
    cin >> n >> k;
    for (int i = 0; i < n ; i++){
        cin >> a;
        s.push(a);
    }
    for (int i = 0; i < k ; i++){
        s.pop();
    }
    if (s.empty() != true){
        cout << s.top();
    }else{
        cout << "empty stack";
    }
    return 0;
}

cout << s.size();


```


# pair

```cpp
#include <iostream>
#include <map>
#include <string>
using namespace std;
int main(){
    pair<string,int> p;
    string str;
    int k;
    cin >> str >> k;
    p = make_pair(str,k);
    cout << p.first << " "<< p. second;
    return 0;
}


#pair 比较
int main(){
    pair<int,int> p1,p2;
    int k1,k2;
    cin >> k1 >> k2;
    p1 = make_pair(k1,k2);
    cin >> k1 >> k2;
    p2 = make_pair(k1,k2);
    if(p1 < p2){
        cout << "Yes";
    }else{
        cout << "No";
    }
    return 0;
}



```


# algorithm

```cpp
#min()

#include <iostream> 
#include <algorithm>
using namespace std;

int main(){
    int a,b;
    cin >> a >> b;
    cout << min(a,b);
    return 0;
}

# max()
cout << max(a,b);

# abs()

int main(){
    int a;
    cin >> a;
    cout << abs(a);
    return 0;
}

# swap()
int main(){
    int a,b;
    cin >> a >> b;
    swap(a,b);
    cout << a << " " << b;
    return 0;
}

# reverse
int main(){
    vector<int> v;
    int n,a;
    cin >> n;
    for(int i = 0; i< n ;i++){
        cin >> a;
        v.push_back(a);
    } 
    reverse(v.begin(),v.end());
    for(int i = 0; i < v.size();i++){
        if(i != 0){
            cout << " ";
        }
        cout << v[i];
    }
    return 0;
}

# string reverse
int main(){
    string s;
    cin >> s;
    reverse(s.begin(),s.end());
    cout << s;    
    return 0;
}



# next_permutation
int main(){
    int n;
    cin >> n;
    vector<int> v;
    for(int i = 1; i <= n ; i++){
        v.push_back(i);
    }
    do {
        for(int i = 0 ; i < n; i++){
            cout << v[i];
            if (i < n-1){
                cout << " ";
            }else{
                cout << endl;
            }
        }
    } while (next_permutation(v.begin(),v.end()));
    return 0;



#fill()
int main(){
    int a[100];
    int n,k;
    cin >> n >> k;
    fill(a,a+n,k);
    for(int i = 0;i < n;i++){
        if(i != n-1){
            cout << a[i] << " ";
        }else{
            cout << a[i];
        }
    }
    return 0;
}



# fill() 
int main(){
    int a[3][5];
    int n=3,m = 5,k;
    cin  >> k;
    fill(&a[0][0],&a[0][0]+n * m,k);
    for(int i = 0;i < 3;i++){
        for(int j = 0; j < m;j++ ){
            if(j != m-1){
                cout << a[i][j] << " ";
            }else{
                cout << a[i][j] << endl;
            }
        }
        
    }
    return 0;
}


# sort 函数

int main(){
    int n,x;
    cin >> n;
    int a[n];
    for(int i = 0; i < n;i++){
        cin >> x;
        a[i] = x;
    }
    sort(a,a+n);
    for(int i = 0; i < n;i++){
        if(i != n-1){
            cout << a[i] << " ";
        }else{
            cout << a[i];
        }
    }
    return 0;
}

# 降序
bool cmp(int a, int b){
    return a > b;
}
int main(){
    int n,x;
    cin >> n;
    int a[n];
    for(int i = 0; i < n;i++){
        cin >> x;
        a[i] = x;
    }
    sort(a,a+n,cmp);
    for(int i = 0; i < n;i++){
        if(i != n-1){
            cout << a[i] << " ";
        }else{
            cout << a[i];
        }
    }
    return 0;
}



# lower_bound 
#include <iostream> 
#include <algorithm>
using namespace std;

int main(){
    int n,x,k;
    cin >> n >> k;
    int a[n];
    for(int i = 0; i < n; i++){
        cin >> x;
        a[i] = x;
    }
    int pos = lower_bound(a, a + n, k) - a;
    if(pos >= n){
        cout << n+1 ;
    }else{
        cout << pos +1;
    }
    return 0;
}


# string 的排序
const int MAXN = 10;
string  str[MAXN];
int main(){
    int n;
    cin >> n;
    int a[n];
    for(int i = 0; i < n;i++){
        cin >> str[i];
    }
    sort(str,str+ n);
    for(int i = 0; i < n;i++){
        cout << str[i] << endl;
    }
    return 0;
}



# 结构体的排序

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

struct Node {
    int x,y;
    Node(int _x ,int _y){
        x = _x;
        y = _y;
    }
};
bool cmp (Node a, Node b){
    if(a.x != b.x){
        return a.x < b.x;
    }else{
        a.y < b.y;
    }
}
int main() {
    vector<Node> v;
    int n,x,y;
    cin >> n;
    for(int i = 0; i < n;i++){
        cin >> x >> y;
        v.push_back(Node(x,y));
    }
    sort(v.begin(),v.end(),cmp);
    for(int i = 0; i < n ; i++){
        cout << v[i].x << " " << v[i].y <<endl;
    }
    return 0;
}



#upper_bound
#include <iostream> 
#include <algorithm>
using namespace std;


    int pos = upper_bound(a, a + n, k) - a;

```