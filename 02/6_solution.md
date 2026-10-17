## 题目 (6.md)

例 5 在凸四边形 ${ABCD}$ 中, ${AB} > {AD},\angle {ABC} = \angle {CDA} = {90}^{ \circ  }$ . 在 ${AB}$ 上取点 $M$ 使得 ${AM} = {AD},{DM}$ 与 ${CB}$ 的延长线交于点 $N$ . 点 $D$ 在 ${AC}$ 上的投影为 $H$ , $C$ 在 ${AN}$ 上的投影为点 $K$ . 证明: $\angle {MHN} = \angle {MCK}$ .

![18_1052_491_392_299_0.jpg](images/18_1052_491_392_299_0.jpg)

图 2-6

证明 如图 2-6,设 ${HN},{CK}$ 与 ${AB}$ 分别交于点 $P, Q$ . 因为 ${AD} = {AM}$ ,所以,

$$
\angle {ADM} = \angle {AMD} = \angle {BMN}.
$$

$$
\text{ 又 }\angle {ADM} + \angle {CDN} = \angle {BMN} + \angle {CND} = {90}^{ \circ  }\text{ , }
$$

故 $\angle {CDN} = \angle {CND}$ ，即 ${CD} = {CN}$ . 在直角 $\bigtriangleup  {ADC}$ 中， 由 ${DH}\bot {AC}$ ，知 $C{D}^2 = {CH} \cdot  {CA}$ ，结合 ${CD} = {CN}$ ，得 $\frac{CH}{CN} = \frac{CN}{CA}$ ，于是 $\bigtriangleup  {CHN} \backsim \; \bigtriangleup  {CNA}$ ，故 $\angle {CNH} = \angle {CAN}$ .

由 ${CK}\bot {AK},{AB}\bot {BN}$ ，知 $\angle {KCA} = \angle {BPN}$ .

由 $A{D}^2 = {AH} \cdot  {AC}$ 及 ${AD} = {AM}$ ，知 $\frac{AM}{AH} = \frac{AC}{AM}$ ，结合 $\angle {HAM} = \angle {CAM}$ ，知 $\bigtriangleup {AHM} \backsim  \bigtriangleup {AMC}$ ，故 $\angle {AMH} = \angle {ACM}$ ，因此由

$$
\angle {BPN} = \angle {AMH} + \angle {MHP} = \angle {KCA} = \angle {ACM} + \angle {MCK}
$$

知 $\angle {MHN} = \angle {MCK}$ . 所以原问题得证.

注:射影定理结合线段相等可导出三角形相似，这一方法在本题中多次用到.

这是一个费解的证明。我能确认每一步的正确性，但我想知道这是怎么想出来的。请为我解释。

---

\begin{solution}

这份解答之所以让人觉得“费解”，是因为它采用了典型的**“综合法”（由因导果）**书写顺序：一上来先设出交点 $P, Q$[cite: 1]，然后抛出两个相似三角形，最后突然用外角定理一步收尾。这种写法抹去了探索的痕迹。

如果用**“结构拆解 + 逆向分析（执果索因）”**的视角还原整个思考过程，你会发现每一步都是高度自然的。

---

### 一、 顺推条件：捕捉“双子相似”结构

在阅读题干时，有经验的解题者会第一时间对“直角三角形斜边上的高”产生条件反射：

1. **射影定理的触发**
   已知 $\angle CDA = 90^\circ$ 且 $DH \perp AC$[cite: 1]，在 $\text{Rt}\triangle ADC$ 中立刻得到两组射影定理关系：
   $$AD^2 = AH \cdot AC, \quad CD^2 = CH \cdot CA$$

2. **条件 $AM = AD$ 的真实意图**
   题目在 $AB$ 上截取 $AM = AD$，直接代入第一个射影定理，就得到了：
   $$AM^2 = AH \cdot AC \implies \frac{AM}{AH} = \frac{AC}{AM}$$
   配合公共角 $\angle HAM = \angle CAM$[cite: 1]，立刻锁定第一组相似（子母相似/反演相似）：
   $$\triangle AHM \sim \triangle AMC \implies \angle AMH = \angle ACM$$

3. **点 $N$ 的几何本质：被伪装的 $CN = CD$**
   既然 $A$ 侧通过 $AM = AD$ 构造了子母相似，那么 $C$ 侧的 $CD^2 = CH \cdot CA$ 怎么用？自然会去寻找与 $CD$ 相等的线段。
   观察 $\angle ADC = 90^\circ$ 和 $\angle MBC = 90^\circ$[cite: 1]，由于 $\triangle ADM$ 是等腰三角形（$AD = AM$），它的两个底角相等，因此它们在两个直角中的余角也必然相等：
   $$\angle CDN = 90^\circ - \angle ADM = 90^\circ - \angle BMN = \angle CND$$
   于是得出 $CN = CD$。你会发现，**题目用“$DM$ 与 $CB$ 延长线交于 $N$”这一操作，本质上只是为了隐蔽地给出 $CN = CD$**。
   一旦识破 $CN = CD$，代入 $CD^2 = CH \cdot CA$ 就会得到完全对称的第二组子母相似：
   $$CN^2 = CH \cdot CA \implies \triangle CHN \sim \triangle CNA \implies \angle CNH = \angle CAN$$

---

### 二、 逆向倒推：交点 $P$ 与最后一步外角是怎么想到的？

拿到上述两组相似后，手里最核心的已知角是 **$\angle AMH = \angle ACM$**，而目标是证明 **$\angle MHN = \angle MCK$**[cite: 1]。怎么把它们联系起来？

1. **观察射线位置，用“拼角”消去公共边**
   * 看右侧：已知角 $\angle ACM$（夹在 $AC, CM$ 之间）和目标角 $\angle MCK$（夹在 $CM, CK$ 之间）**恰好共用一条边 $CM$**[cite: 1]！把它们加起来，中间的边 $CM$ 就被消掉了，合成为一个干脆的大角 $\angle KCA$[cite: 1]：
     $$\angle MCK = \angle KCA - \angle ACM$$
   * 看左侧：既然 $\angle ACM$ 和 $\angle AMH$ 相等，为了把 $\angle AMH$（夹在 $AB, HM$ 之间）和另一个目标角 $\angle MHN$（夹在 $HM, HN$ 之间）用同样的方式捆绑起来，**我们也应该把这两个共用边 $HM$ 的角加起来**[cite: 1]！

2. **交点 $P$ 的自然诞生**
   把“直线 $AB$ 与 $HM$ 的夹角（$\angle AMH$）”和“$HM$ 与直线 $HN$ 的夹角（$\angle MHN$）”加起来，得到的是什么？
   **正是直线 $AB$ 与直线 $HN$ 的夹角！**
   为了在图上表示出直线 $AB$ 与直线 $HN$ 的夹角，我们才顺理成章地设 $HN$ 与 $AB$ 交于点 $P$[cite: 1]。在 $\triangle PMH$ 中利用外角定理[cite: 1]，就有：
   $$\angle MHN = \angle BPN - \angle AMH$$
   所以，**点 $P$ 绝不是凭空猜出来的辅助点，而是为了表示“$AB$ 与 $HN$ 的夹角”自动产生的交点**。

3. **在直角三角形中完成合龙**
   既然 $\angle AMH = \angle ACM$，要证 $\angle MHN = \angle MCK$，现在只需要证明刚才合成的两个大角相等：
   $$\angle BPN = \angle KCA$$
   这两个角各自处在一个现成的直角三角形中[cite: 1]：
   * 在 $\text{Rt}\triangle PBN$ 中（因为 $AB \perp BN$[cite: 1]），$\angle BPN = 90^\circ - \angle CNH$；
   * 在 $\text{Rt}\triangle AKC$ 中（因为 $CK \perp AN$[cite: 1]），$\angle KCA = 90^\circ - \angle CAN$。

   因此，要证 $\angle BPN = \angle KCA$，只需证它们的余角相等，即 **$\angle CNH = \angle CAN$**——而这恰好就是我们在第一阶段由 $\triangle CHN \sim \triangle CNA$ 得出的结论！至此，双向推理完美合龙。

---

### 三、 原解答中的两处“跳步与冗余”说明

读懂了上面的思路，你还能顺便看穿原书解答在排版和改写时留下的两个小瑕疵：

1. **被遗忘的点 $Q$**：解答第一句写道“设 $HN, CK$ 与 $AB$ 分别交于点 $P, Q$”[cite: 1]，但后文直到证毕都再也没有出现过字母 $Q$。这是因为在 $\triangle ACN$ 中，$AB \perp CN$ 且 $CK \perp AN$，点 $Q$ 其实是 $\triangle ACN$ 的**垂心**[cite: 1]。作者最初在草稿上很可能是利用对顶角与直角三角形相似先写出 $\angle KCA = \angle BQC$，再去和 $\angle BPN$ 比较；定稿时简化了表述，却忘了删掉开头的点 $Q$[cite: 1]。
2. **因果关系的省略**：原解答写“于是 $\triangle CHN \sim \triangle CNA$，故 $\angle CNH = \angle CAN$。由 $CK \perp AK, AB \perp BN$，知 $\angle KCA = \angle BPN$”[cite: 1]。这两句之间其实省略了“等角的余角相等”这一关联词，容易让读者误以为第二句是独立推出来的。

---

### 四、 更高维度的视角：这道题是怎么命制出来的？

如果从**反演几何（或正交圆）**的视角看，这道题的构造背景非常清晰：

* 以 $A$ 为圆心、$AD$ 为半径作圆 $\omega_A$（过点 $D, M$[cite: 1]）；以 $C$ 为圆心、$CD$ 为半径作圆 $\omega_C$（过点 $D, N$[cite: 1]）。
* 因为 $\angle ADC = 90^\circ$，所以 $\omega_A$ 与 $\omega_C$ 是**正交圆**（$CD$ 切 $\omega_A$ 于 $D$，$AD$ 切 $\omega_C$ 于 $D$），$DH \perp AC$ 所在的直线就是两圆的根轴[cite: 1]。
* 在关于 $\omega_A$ 的反演变换下，点 $H$ 与点 $C$ 互为反演点；因为 $M \in \omega_A$，直接由反演性质得 $\triangle AHM \sim \triangle AMC$。
* 在关于 $\omega_C$ 的反演变换下，点 $H$ 与点 $A$ 互为反演点；因为 $N \in \omega_C$，直接由反演性质得 $\triangle CHN \sim \triangle CNA$。

命题人正是以这两个正交圆对点 $H$ 的双重反演对称性为内核，擦去圆弧，再用直角与垂线包装出了这道平面几何题。

\end{solution}