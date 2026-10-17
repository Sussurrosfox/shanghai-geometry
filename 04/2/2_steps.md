# 2 — 分步证明文字

## 步骤 0：已知条件与问题导入

已知条件：点 $D$ 在 $\triangle ABC$ 的边 $BC$ 上，且满足 $AD > BC$；点 $E$ 在边 $AC$ 上，满足比例关系式：
      $\frac{AE}{EC} = \frac{BD}{AD - BC}$
      求证目标：证明 $AD$ > $BE$。
      几何困境：线段 $AD$ 与 $BE$ 既不共端点，也不在同一个三角形中，无法直接利用三角形边角不等式进行比较。
      核心突破口：通过平移，将线段 $BE$ 转移到与 $AD$ 共顶点的三角形中！

## 步骤 1：① 延长底边：构造关键线段 CF 与 FG

如图所示，在底边直线上进行几何构造：
      1. 延长 $BC$ 至点 $F$，使得 $CF = AD - BC$；
      2. 继续延长至点 $G$，使得 $FG = BD$。
      全长核算：
      • $BC + CF = BC + (AD - BC) = AD$
      • 线段 $DG$ 的总长为：
      $DG = DC + CF + FG = (BD + DC) + CF = BC + CF = AD$
      因此，我们巧妙构造出了线段等量关系：$DG = AD$！

## 步骤 2：② 比例转化：由平行线分线段成比例得 EF ∥ AG

根据题目给出的比例条件 $\frac{AE}{EC} = \frac{BD}{AD - BC}$，将构造的等长代入：
      • 构造中 $BD = FG$；
      • 构造中 $AD - BC = CF$。
      因此原比例式等价转化为：
      $\frac{AE}{EC} = \frac{FG}{CF}$
      在 $\triangle ACG$ 中，点 $E$ 位于边 $AC$ 上，点 $F$ 位于边 $CG$ 上。
      根据平行线分线段成比例定理的逆定理，两边截出的线段对应成比例，立即推出：
      $EF \parallel AG$

## 步骤 3：③ 平移构造：平行四边形 BDKE 使 BE = DK

过点 $E$ 作直线平行于底边 $CG$，交线段 $AG$ 于点 $K$，即 $EK \parallel CG$：
      1. 在四边形 $FEKG$ 中，$EF \parallel KG$ 且 $EK \parallel FG$，故 $FEKG$ 为平行四边形；
      2. 从而其对边平行且相等：$EK \xlongequal{\parallel} FG$；
      3. 又由第一步构造知 $FG = BD$ 且都在底边同一直线上，所以：
      $EK \xlongequal{\parallel} BD$
      四边形 $BDKE$ 有一组对边平行且相等，因此 $BDKE$ 为平行四边形！
      连接 $DK$，则对边平行且相等：$DK = BE$。
      至此，我们成功将线段 $BE$ 沿水平方向平移到了 $DK$！

## 步骤 4：④ 角度关系：等腰 △ADG 底角与外角不等式

现在将几何焦点集中到点 $D, A, G, K$ 构成的角度关系：
      1. 在第 ① 步中已算出：
      $DG = DC + CF + FG = BC + CF = AD$
      因此 $\triangle ADG$ 是以 $D$ 为顶点的等腰三角形（$AD = DG$）。
      根据等腰三角形两底角相等，有：
      $\angle DAK = \angle DAG = \angle G$
      2. 考察 $\triangle DKG$：点 $K$ 在线段 $AG$ 上，角 $\angle AKD$ 是 $\triangle DKG$ 在顶点 $K$ 处的外角。
      由三角形外角大于任何一个不相邻的内角，立即得到：
      $\angle AKD > \angle G$
      将 $\angle G = \angle DAK$ 代入，即可导出关键角的不等关系：
      $\angle AKD > \angle DAK$

## 步骤 5：⑤ 得出结论：在 △ADK 中大角对大边 AD > BE

聚焦三角形 $\triangle ADK$：
      在 $\triangle ADK$ 中，由第 ④ 步已知：
      $\angle AKD > \angle DAK$
      根据平面几何基本定理「在同一个三角形中，大角对大边」：
      角 $\angle AKD$ 所对的边为 $AD$，角 $\angle DAK$ 所对的边为 $DK$。因此：
      $AD$ > $DK$
      最后，代入第 ③ 步中平移平行四边形给出的对边等量关系 $DK = BE$，立即得到：
      
        $AD > BE$
      
      结论证明完毕！
      方法总结：通过构造延长线和平行四边形，巧妙实现了线段平移，将原本分散在空间的两条线段转化到同一三角形 $\triangle ADK$ 中，利用等腰外角与大角对大边达成证明。
