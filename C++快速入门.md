```cpp
#include <cstdio>
```
只要涉及任何的输入输出，就需要stdio库！


# 刷题总结

	刷题步骤
1. 先认真审题（确定输入输出，一些边界要求）
2. 先测试，通过之后先记录自己的题解
3. 看看别人的题解是不是更好


# 顺序结构

```cpp
#2.1 直接输出`Hello Sunny Why!`

#include <iostream>

using namespace std;
int main() {
	cout<<"Hello Sunny Why!"<<endl;
}

```

	2.2 

```cpp

# 整型int 输入输出 10^(9)
int main() {
	int a;
	scanf("请输入一个整数%d",&a);
	printf("然后输出它本身%d",a);
	return 0;
}

# 长整型 long long 输入输出 10^18
int main() {
	long long a;
	scanf("请输入一个长整型%lld",&a);
	printf("然后输出它本身%lld",a);
	return 0;
	
}

#浮点数double输入输出 10^3
int main() {
	double a; //long float
	scanf("请输入一个浮点数%lf",&a);
	printf("然后输出它本身%lf",a);
	//要求输出保留两位小数
	printf("保留两位小数%2f",a);
	return 0;
	
}
# 字符的输入输出
int main() {
	char  c; 
	scanf("请输入一个字符%c",&c);
	printf("然后输出它本身%c",c);
	return 0;
	
}

# 换行符：输入两个正整数，然后分两行输出它们。
int main() {
	int a,b;
	scanf("请输入两个整数：%d %d",%a,%b)
	printf("分成两行输出：%d \n %d",a,b)
	return 0,
}

#强制类型转换
#include <iostream>
using namespace std;
int main() {
    int a,b;
    scanf("%d %d",&a,&b);
    printf("%d\n%.2f",a/b,(double)a/b);
    return 0;
}



```




```cpp

# 输出周长
#include <cstdio>

int main() {
    double r;
    const float PI = 3.14;
    scanf("%lf",&r);
    printf("%.2f",2*r*PI);
    return 0;
}

#自增运算符

#include <cstdio>
int main() {
    int n;
    scanf("%d",&n);
    printf("%d",++n);
    return 0;
}



#条件运算符
#include <cstdio>

int main() {
    int A,B;
    scanf("%d %d ",&A,&B);
    if (A >= B){
        printf("A >= B");
    }else{
        printf("A < B");
    }
    return 0;
}


//别人的更加简洁
int main() {
    int a, b;
    scanf("%d%d", &a, &b);
    printf(a >= b ? "A >= B" : "A < B");
    return 0;
}


```

```cpp
#日期时间输入输出I
#include <cstdio>

int main() {
    int YYYY,MM,DD,HH,MI,SS;
    scanf("%d-%d-%d %d:%d:%d",&YYYY,&MM,&DD,&HH,&MI,&SS);
    printf("%d\n%d\n%d\n%d\n%d\n%d\n",YYYY,MM,DD,HH,MI,SS);
    return 0;
}

#高位不满对应位数时用 0 补齐
#include <cstdio>

int main() {
    int YYYY,MM,DD,HH,MI,SS;
    scanf("%d-%d-%d %d:%d:%d",&YYYY,&MM,&DD,&HH,&MI,&SS);
    printf("%04d\n%02d\n%02d\n%02d\n%02d\n%02d\n",YYYY,MM,DD,HH,MI,SS);
    return 0;
}


# getchar 
#include <cstdio>

int main() {
    int n;
    char c;
    scanf("%d\n%c",&n,&c);
    printf("%d\n%c",++n,c);
    return 0;
}

//还可以使用getchar，可以接收enter输入
getchar()
c = getchar()
printf("%c",c)
```


	常见的math函数
```cpp

#include <math.h>

fabs(x) //绝对值function of absolute  value
floor(x) //地板取整数
ceil(x) //天花板取整
pow(x,5) //输出x^5
sqrt(x) //square root平方根
round(x) //四舍五入
 (int)round(3.14)//记得取整

//左边参数要求是幅度制
x = pi* (1/3)
sin(x)   asinx(x)
cos(x)   acos(x)
tan(x)    atan(x)
```

```cpp
#include <cstdio>
#include <math.h>

//浮点数取整，占位符：%.0f

int main() {
    double f;
    scanf("%lf",&f);
    // 这里可以添加一些注释
    printf("%.2f %.0f %.0f %.0f %.2f",fabs(f),floor(f),ceil(f),round(f),pow(f,5) );
    return 0;
}


#include <cstdio>
#include <math.h>

int main() {
    double d;
    scanf("%lf",&d);
    printf("%.2f %.2f",sqrt(d),log(d));
    return 0;
}

```



# 3、选择结构


```CPP

int main() {
	int n=0;
if(n){ //等价于 if (n!=0)
	printf("n is not zero! \n");
}else{
	printf("n is zero! \n");
}
	retutn 0;
}


# 嵌套if



# switch-case-break


#include <cstdio>

int main() {
    int n;
    scanf("%d",&n);
    //条件放这里哦
    switch (n){
    //条件的结果放在case后
        case 0:
            printf("Zero");
            //一定要break！
            break;
        case 1:
            printf("One");
            break;
        case 2:
            printf("Two");
            break;
        case 3:
            printf("Three");
            break;
        case 4:
            printf("Four");
            break;
        case 5:
            printf("Five");
            break;
        //else在这要写成default
        default :
            printf("Greater than 5");
            break;
    }
    return 0;
}






```


```cpp
#奇偶判断
#include <cstdio>

int main() {
    int n ;
    scanf("%d",&n);
    if(n%2 == 0){
        printf("Even Number");
    }else{
        printf("Odd Number");
    }

    return 0;
}


#嵌套
#include <cstdio>
int main() {
    int n;
    scanf("%d",&n);
    if(n <0){
        printf("Negative Number");
    }else{
        if(n%2) {
            printf("Odd Number");
        }else{
            printf("Even Number");
        }
    }

    return 0;
}```





# 4.循环结构



while和do - while(先do一次之后再判断)

for 是yyds！

break and  continue

```cpp

for (int i =1;i<=5;i++) {
	if(i % 2 ==1) continue //i是奇数咱就不加 
}


```

```cpp
#相加
int main() {
    int n;
    int sum = 0;
    int i =0;
    scanf("%d",&n);
    while(i <= n){
        sum = sum +i;
        i++;
    }
    printf("%d",sum);
    return 0;
}

#break
int main() {
    int n;
    int sum = 0;
    scanf("%d",&n);
    for(int i = 1; i <= n; i++) {
        sum += i;
        if (sum > 2000) {
            break;
        }
    }
    printf("%d",sum);
    return 0;
}


# continue
int main() {
    int n;
    scanf("%d",&n);
    int sum =0 ;
    for (int i = 1; i <= n; i++){
        if (i %3 ) {
        sum = sum +i;
        }else {
            continue;
        }
    }
    printf("%d",sum);
    return 0;
}

int main() {
    int n;
    scanf("%d",&n);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++){
            printf("%d",j);
            //行末不允许有多余的空格。
            printf(j < n ? " ": "\n");
        }
    }
    return 0;
}

#梯度
int main() {
    int n;
    scanf("%d",&n);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++){
            printf("%d",j);
            //行末不允许有多余的空格。
            printf(j < i ? " ": "\n");
        }
    }
	return 0;
}

#倒三角
int main() {
    int n;
    scanf("%d",&n);
    for (int i = 1; i <=n ;i++){
        for (int j =1; j <= n-i+1;j++) {
            printf("%d",j);
            printf(j< (n-i+1) ? " ": "\n");
        }
    }
	return 0;
}
```


# 5.数组


```cpp

数组初始化：
后面没赋值的就是默认0
但是一开始整个数组都没赋值，里面的数就是随机值
int a[10] = {1,2,3,4,5,6,7,8};

全部赋值为0
int a[10] = {0};


# 顺推和逆推：a[i]和 a[i+1]之间递推

int a[10]
scanf("%d",&a[0])
for(int i=1 ;i<10;i++){
	a[i] = a[i-1] * 2;


}


#末行不允许多余空格哈哈哈

if (i<n-1) {
        printf(" ");
    }
    


#定义数组最大长度，
const int MAXN = 10;
int a[MAXN];
int main() {
    int n;
    scanf("%d",&n);
    for (int i = 0; i < n; i++){
        scanf("%d",&a[i]);
    }
    
    for (int i = 0; i < n; i++){
        printf("%d",a[i]);
        if (i<n-1) {
            printf(" ");
            }
    }
    return 0;
}
//注意括号是否缺少，只要对不上都编译不通过
    ```



```cpp
#输入输出arr

int main() {
    int n;
    cin >> n;
    int arr[n];
    for (int i=1 ; i<= n;i++){
        cin >> arr[i];
    }
    for (int i = 1; i <= n; i++){
        if(i < n) {
            cout << arr[i] << " ";
        }else{
            cout << arr[i];
        }
    }
    return 0;
}

#memset
#include <cstdio>
#include <iostream>
#include <string.h>
using namespace std;
int main() {
    int x,A[1];
    cin >> x;
    memset(A,x,sizeof(A));
    cout << A[0];
    return 0;
}




```





	字符串输入输出

```cpp
#可以输入空格的
#include <cstdio>
#include <iostream>
using namespace std;
int main() {
    char str[50];
    cin.getline(str,51);
    cout << str;
    return 0;
}

#以换行符为结尾的
#连续输入三行，输出三行，可以一个循环就搞定，可以输入一行，立刻输出一行（无需输三行再输出三行）
#include <cstdio>
#include <iostream>
using namespace std;
const int MAXN = 51;//多一个存放\0
char arr[MAXN];

int main() {
    int n;
    cin >> n;
    getchar();
    for (int i=1;i <=n;i++){
        cin.getline(arr,MAXN);
        cout << arr << endl;
    }
    return 0;
}

#字符串长度
#include <cstdio>
#include <string.h>
#include <iostream>

using namespace std;
int main() {
    char str[51];
    cin.getline(str,51);
    cout << strlen(str);
    return 0;
}

#直接比较字符串！ cpp牛逼
#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

const int MAXN = 51;
int main() {
    string a, b;
    cin >> a;
    cin >> b;
    if (a == b){
        cout << "=";
    }else if (a > b){
        cout << ">";
    }else{
        cout << "<";
    }
    return 0;
}

# 字符串拼接,直接相加
#include <iostream>
#include <string>
using namespace std;
int main() {
    string a,b;
    cin >> a;
    cin >> b;
    cout << a+b;
    return 0;
}
```


# 必须马上马上！！！检查代码

## 冒泡排序


bubble sort
冒泡排序本质：交换(需要实现交换)

复杂度：n^2

```cpp
#实现交换

func swap (int *a,int *b){
	int temp = &a;
	&a = &b;
	&b = temp;
	
}

for (int i =0; i<len(a[]);i++){
	if (a[i]>a[i+1]){
		swap(a[i],a[i+1]);
	}
}



#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 100;
int a[MAXN];

#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 100;
int a[MAXN];

int main() {
    int n;
    scanf("%d",&n);
    for (int i = 0; i <= n-1;i++){
        scanf("%d",&a[i]);
    }
    //i和j的初始一定要标清楚，从0 还是1开始，j的终止条件！
    for (int i = 1; i <= n-1;i++){
        for(int j=0; j< n-i ; j++){
            if(a[j]>a[j+1]) {
                swap(a[j],a[j+1]);
            }
        }
    }
    for (int i = 0; i < n;i++){
        printf("%d",a[i]);
        if (i < n-1){
            printf(" ");
        }
    }
	return 0;
}


#二维数组

int main() {
    int n,m;
    scanf("%d%d",&n,&m);
    for (int i =0; i <= n-1;i++){
        for(int j=0; j<=m-1;j++){
            scanf("%d",&a[i][j]);
        }
    }
    for (int i =0; i <= n-1;i++){
        for(int j=0; j<=m-1;j++){
            printf("%d",a[i][j]);
            //末尾换行还是空格？
            printf(j < m-1 ? " ": "\n");
        }
    }
    return 0;
}

```

	重要说明
数组数据量大的话，最好放在函数外面定义，数组存放在
函数主要存放在系统栈中，申请的空间较小，如果把数组放在 里面，申请的空间就太大了，hold不住

	memset

对数组中的每个元素赋同样的值（0，-1）
如果想要赋值成其他值，使用fill函数



```cpp
# memory set内存设置，
#ptr是需要设置的内存块指针、设置的值，设置的字节数


void *memset(void *ptr, int value, size_t num);

int a[10] = {0}

memset(a,-1,sizeof(a));

for (int i =0;i<10;i++){
	printf("%d",a[i]);
}
```


- 字符串以空格作为结尾标志
getchar( )-输入单个字符   putchar( )-输出单个字符

gets输入一行字符串
puts输出一行字符串




# 6.函数

```cpp
#实现increase

#include <cstdio>
int increase(int x) {
    x++;
    return x;
}

int main() {
    int n;
    scanf("%d",&n);
    int x = increase(n);
    printf("%d %d",x,n);
    return 0;
}


# 求max3

#include <cstdio>
#include <iostream>

//m = (a > b ? a :b);
//这样写真的很棒！
using namespace std;

int max(int a, int b,int c) {
    int m;
    m = (a > b ? a :b);
    m = (m > c ? m : c);
    return m;
}
int main() {
    int a,b,c;
    cin >> a >> b >> c;
    cout << max(a,b,c);
    return 0;
}


#交换指针
void swap(int* a,int* b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}
int main() {
    int a ,b;
    cin >> a;
    cin >> b;
    swap(&a,&b);
    cout << a << " "<< b;
    return 0;
}



```

# 7、指针

```cpp

#交换指针 变量
using namespace std;
void swap(int* a,int* b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}
int main() {
    int a ,b;
    cin >> a;
    cin >> b;
    swap(&a,&b);
    cout << a << " "<< b;
    return 0;
}



#引用
#include <cstdio>
#include <iostream>
using namespace std;

void increase (int &x){
    ++x;
}
int main() {
    int n;
    cin >> n;
    increase (n);
    cout << n;
    return 0;
}



```

# 8.结构体

```cpp
#不同参数的构造函数
#include <cstdio>
#include <iostream>
using namespace std;

struct Point {
    int x,y;
    Point(){}
    Point(int _x,int _y) {
        x = _x;
        y = _y;
    } 
} point;
int main() {
    int x,y;
    cin >> x >> y;
    point = Point(x,y);
    cout << point.x << " " << point.y;
    return 0;
}

#输入些其他内容
struct Student {
    int id;
    char name[15];
    Student (int _id, char _name[]) {
        id = _id;
        strcpy(name,_name);
    }
};

int main() {
    int id;
    char name[15];
    cin >> id;
    scanf("%s",name);
    Student student = Student(id,name);
    cout << student.id << endl;
    cout << student.name << endl;
    return 0;
}

#指针传递
struct Node {
    int id;
    Node* left;
    Node* right;
    Node(int _id, Node* _left, Node* _right) {
        id = _id;
        left = _left;
        right = _right;
    }
};
int main() {
    int id1,id2,id3;
    cin >> id1 >> id2 >> id3;
    Node node1 = Node(id1,NULL,NULL);
    Node node2 = Node(id2,NULL,NULL);
    Node node3 = Node(id3,&node1,&node2);
    cout << node3.left->id << " " << node3.right->id;
    return 0;
}


```



# 9.黑盒测试



# 10 其他内容

```cpp
# cin cout

const int MAXN = 100;
char str[MAXN];
int main() {
    int n;
    double d;
    cin >> n >> d ;
    getchar();
    cin.getline(str,MAXN);
    cout<<n<<endl;
    cout<< setiosflags(ios::fixed)<<setprecision(2)<<d<<endl;
    cout << str;
    return 0;


#浮点数进度比较
# eps   epsilon

#include <cstdio>
#include <iostream>
#include <math.h>
using namespace std;
#define More(a,b) ((a)-(b)>(eps))
#define Less(a,b) ((a)-(b)<(-eps))
const double eps = 1e-8;

int main() {
    int A,B,C,D;
    cin >> A >> B >> C >> D;
    double result1,result2;
    result1 = A* asin(sqrt(B)/2);
    result2 = C* asin(sqrt(D)/2);
    if (More(result1,result2)) {
        cout << "1";
    }else if (Less(result1,result2)){
        cout << "2";
    }else {
        cout << "0";
    }
    return 0;
}


}```