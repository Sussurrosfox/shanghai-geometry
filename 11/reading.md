## 阅读欣赏

## 从任意多边形构造正多边形

在向量与复数方法一讲的例 3 中, 我们证明了如下命题:

(1)对于 $\bigtriangleup {ABC}$ ，由 ${AB},{BC},{CA}$ 分别向三角形外侧作一个等边三角形，这三个等边三角形的中心分别为 $P, Q, R$ ，则 $\bigtriangleup {PQR}$ 是等边三角形.

(2)对于凸四边形 ${ABCD}$ ，由 ${AB},{BC},{CD},{DA}$ 分别向四边形外侧作一个正方形，这四个正方形的中心分别为 $P, Q, R, S$ ，则 ${PR}$ 与 ${QS}$ 垂直且相等.

不难发现，在(2)中，如果分别取 ${PQ},{QR},{RS},{SP}$ 的中点，则这四个中点构成了一个正方形的四个顶点. 于是我们便可以考虑将上述命题推广至任意 $n$ 边形的情形. 1942 年，纽曼(B. H. Neumann)在文章 A Remark on Polygons 中给出了一种推广形式，与例 3 的思路类似，其证明也使用了复数.

现设复平面上有 $n$ 个点 ${A}_1,{A}_2,\cdots ,{A}_n$ . 对于复数 ${z}_1$ ，在复平面作出点

$$
{A}_{12} = \left( {1 - {z}_1}\right) {A}_1 + {z}_1{A}_{2}.
$$

利用复数的几何意义,可知点 ${A}_1,{A}_2,{A}_{12}$ 就与点 $0,1,{z}_1$ 同向相似. 类似地可以作出点 ${A}_{23},{A}_{34},\cdots ,{A}_{n1}$ .

再取复数 ${z}_2$ ,令 ${A}_{123} = \left( {1 - {z}_2}\right) {A}_{12} + {z}_2{A}_{23}$ ,进一步可以再定义 ${A}_{234},{A}_{345},\cdots$ , ${A}_{n12}$ . 依此类推,取复数 ${z}_3,{z}_4,\cdots ,{z}_{n - 1}$ ,直到定义了点 ${A}_{{123}\cdots n},{A}_{{234}\cdots 1},\cdots$ , ${A}_{{n12}\cdots \left( {n - 1}\right) }$ .

现在我们记 ${z}_1^{\prime } = 1 - {z}_1,{z}_2^{\prime } = 1 - {z}_2,\cdots$ 再引入算子 $T$ ,表示将 ${A}_k$ 变换为 ${A}_{k + 1}\left( {k = 1,2,\cdots , n\text{ ,其中 }{A}_{n + 1} = {A}_{1}}\right)$ ,即 $T{A}_k = {A}_{k + 1}$ . 此时便有

$$
{A}_{12} = {z}_1^{\prime }{A}_1 + {z}_1{A}_2 = \left( {{z}_1^{\prime } + {z}_{1}T}\right) {A}_{1}.
$$

而

$$
{A}_{123} = {z}_2^{\prime }{A}_{12} + {z}_2{A}_{23}
$$

$$
= {z}_2^{\prime }\left( {{z}_1^{\prime } + {z}_{1}T}\right) {A}_1 + {z}_2\left( {{z}_1^{\prime } + {z}_{1}T}\right) {A}_2
$$

$$
= \left( {{z}_2^{\prime } + {z}_{2}T}\right) \left( {{z}_1^{\prime } + {z}_{1}T}\right) {A}_{1}.
$$

通过归纳不难得到

$$
{A}_{{123}\cdots n} = \left( {\mathop{\prod }\limits_{k = 1}^{n - 1}\left( {{z}_k^{\prime } + {z}_{k}T}\right) }\right) {A}_{1}.
$$

①

接下来,我们考虑 $n$ 次单位根 $\varepsilon  = \cos \frac{2\pi }{n} + \mathrm{i}\sin \frac{2\pi }{n}$ ,则 $\varepsilon ,{\varepsilon }^2,\cdots ,{\varepsilon }^{n - 1}$ 是多项式 $P\left( z\right)  = {z}^{n - 1} + {z}^{n - 2} + \cdots  + z + 1$ 的所有根. 再令

$$
{z}_k = \frac{1}{1 - {\varepsilon }^k}\left( {k = 1,2,\cdots , n - 1}\right) .
$$

代入①式得

$$
{A}_{{123}\cdots n} = \left( {\mathop{\prod }\limits_{k = 1}^{n - 1}\frac{T - {\varepsilon }^k}{1 - {\varepsilon }^k}}\right) {A}_1
$$

$$
= \frac{P\left( T\right) }{P\left( 1\right) }{A}_1 = \frac{1}{n}\left( {{T}^{n - 1} + {T}^{n - 2} + \cdots  + T + 1}\right) {A}_1
$$

②

$$
= \frac{1}{n}\left( {{A}_n + {A}_{n - 1} + \cdots  + {A}_2 + {A}_1}\right) .
$$

也就是 ${A}_{{123}\cdots n}$ 恰是 ${A}_1,{A}_2,\cdots ,{A}_n$ 的重心 $G$ . 注意到 ②式的右端是轮换对称的， 这表明类似作出的点 ${A}_{{234}\cdots 1},\cdots ,{A}_{{n12}\cdots \left( {n - 1}\right) }$ 都是重心 $G$ . 最后利用作图过程反推可知第 $n - 2$ 步作出的 $n$ 个点一定是正 $n$ 边形的顶点.

