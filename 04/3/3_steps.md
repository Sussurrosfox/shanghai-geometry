# 3 — 分步证明文字

## 步骤 0：题设几何构型与已知条件

已知 Γ 为 △ABC 的外接圆，在 B, C 处的切线相交于点 T。
      作图 取 BC 中点 M，连接 AT；过 A 作 AS ⊥ AT 交直线 BC 于点 S。
      割线 点 B₁, C₁ 在割线 ST 上（B₁, B 位于中垂线同侧），满足 TB₁ = TC₁ = TB。
      目标 证明：△AB₁C₁ ∽ △ABC。

## 步骤 1：① 陪位中线性质 ∠BAT = ∠MAC

连接中线 AM。
      因为外接圆在 B, C 处的切线交于 T，由陪位中线性质，直线 AT 是 △ABC 的 A-陪位中线（与中线 AM 关于 ∠BAC 的角平分线轴对称）。
      
        由此立即得到等角关系：
        ∠BAT = ∠MAC

## 步骤 2：② 正弦定理导出边比 TC₁/AT = MC/AM

由弦切角定理可知 ∠TBC = ∠BAC。于是：
      ∠TBA = ∠TBC + ∠CBA = ∠BAC + ∠CBA = 180° − ∠ACB。
      在 △TAB 与 △AMC 中分别运用正弦定理：
      
        TBAT
        = sin ∠BATsin ∠TBA
        = sin ∠MACsin(180° − ∠ACB)
        = sin ∠MACsin ∠ACB
        = MCAM
      
      
        代入条件 TC₁ = TB，得出关键夹边比：
        
          TC₁AT
          = MCAM
           （即 
          TC₁MC
          = ATAM）

## 步骤 3：③ 四点共圆得 ∠C₁TA = ∠CMA

因为 TB = TC 且 M 为 BC 中点，所以 TM ⊥ BC，即 ∠TMS = 90°。
      又由题设作垂线，知 ∠TAS = 90°。
      在四边形 AMTS 中，两对角均为 90°，故 A, M, T, S 四点共圆（以 ST 为直径）。
      
        由同圆内同弧 AS 所对圆周角相等，立即得出：
        ∠STA = ∠SMA  ⇒  ∠C₁TA = ∠CMA

## 步骤 4：④ 侧翼相似 △ATC₁ ∽ △AMC

在 △ATC₁ 与 △AMC 中：
      ① 夹角对应相等：∠C₁TA = ∠CMA（由步骤 ③）；
      ② 两夹边成比例：TC₁AT = MCAM（由步骤 ②）。
      
        根据两边成比例且夹角相等的判定定理（SAS）：
        △ATC₁ ∽ △AMC
        因此：AC₁AC = ATAM，且 ∠TAC₁ = ∠MAC。

## 步骤 5：⑤ 对称推导与顶角合成

同理，在另一侧对称地有 TB₁ = TB 且 MB = MC。
      由完全对称的推导可得：△AB₁T ∽ △ABM。
      由此得出：AB₁AB = ATAM，且 ∠B₁AT = ∠BAM。
      
        将两角相加，合成大顶角：
        ∠B₁AC₁ = ∠B₁AT + ∠TAC₁ = ∠BAM + ∠MAC = ∠BAC
        且两边比相等：
        AB₁AB = AC₁AC = ATAM

## 步骤 6：✦ 得出最终结论 △AB₁C₁ ∽ △ABC

在 △AB₁C₁ 与 △ABC 中：
      ① 顶角相等：∠B₁AC₁ = ∠BAC；
      ② 对应夹边成比例：AB₁AB = AC₁AC。
      
        根据两边成比例且夹角相等的判定定理，立即得出：
        △AB₁C₁ ∽ △ABC
        原命题获证！✦
