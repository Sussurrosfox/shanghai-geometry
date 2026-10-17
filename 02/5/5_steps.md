# 5 — 分步证明文字

## 步骤 0：已知条件与几何构型

在锐角 $\triangle ABC$ 中，外接圆为 $\odot O$。点 $A_1, B_1, C_1$ 分别在边 $BC, CA, AB$ 上。
    作 $\triangle AB_1C_1, \triangle A_1BC_1, \triangle A_1B_1C$ 的外接圆，与 $\odot O$ 分别交于另一点 $A_2, B_2, C_2$。
    同时取 $A_1, B_1, C_1$ 关于边中点的对称点 $A_3, B_3, C_3$。
    求证：$\triangle A_2B_2C_2 \sim \triangle A_3B_3C_3$

## 步骤 1：① 圆周角定理与第一组相似

连接 $A_2A, A_2B_1, A_2C, A_2B, A_2C_1$。
    在圆 $AB_1C_1A_2$ 与圆 $ABC$ 中，同弧所对圆周角满足：
    $\angle C_1A_2B_1 = \angle BAC = \angle BA_2C$
    $\angle A_2B_1C_1 = \angle A_2AC_1 = \angle A_2CB$
    两角对应相等，得出第一组相似三角形：
    $\triangle B_1A_2C_1 \sim \triangle CA_2B$
    $\implies \dfrac{B_1A_2}{CA_2} = \dfrac{A_2C_1}{A_2B} = \dfrac{B_1C_1}{CB} \quad \text{①}$

## 步骤 2：② 托勒密定理与中点对称线段转化

分别对圆内接四边形 $AB_1C_1A_2$ 与 $ACBA_2$ 应用托勒密定理：
    $AA_2 \cdot B_1C_1 = B_1A_2 \cdot AC_1 - A_2C_1 \cdot AB_1$
    $AA_2 \cdot BC = A_2C \cdot AB - A_2B \cdot AC$
    代入 ① 式比例消去 $AA_2$：
    $\dfrac{A_2C}{A_2B} = \dfrac{AC - AB_1}{AB - AC_1} = \dfrac{CB_1}{BC_1}$
    由中点对称性，$CB_1 = AB_3,\; BC_1 = AC_3$：
    $\dfrac{A_2C}{A_2B} = \dfrac{AB_3}{AC_3}$

## 步骤 3：③ 两边夹角判定相似 $\triangle BA_2C \sim \triangle C_3AB_3$

在 $\triangle BA_2C$ 与 $\triangle C_3AB_3$ 中：
    两边成比例：$\dfrac{A_2C}{AB_3} = \dfrac{A_2B}{AC_3}$；
    对应夹角相等：$\angle CA_2B = \angle BAC = \angle B_3AC_3$。
    由两边成比例且夹角相等判定：
    $\triangle BA_2C \sim \triangle C_3AB_3$
    $\implies \mathbf{\angle A_2CB = \angle AB_3C_3}$
    同理对 $B_2$ 对称推导可得：$\mathbf{\angle B_2CA = \angle BA_3C_3}$。

## 步骤 4：④ 圆心角与圆周角转换锁定顶点角

在圆 $O$ 中，圆心角与圆周角关系满足：
    $\angle A_2C_2B_2 = \frac{1}{2}\angle A_2OB_2 = \angle A_2CB + \angle B_2CA - \angle ACB$
    将步骤 ③ 导出的对应角代入：
    $\angle A_2C_2B_2 = \angle AB_3C_3 + \angle BA_3C_3 + (\angle BAC + \angle ABC - 180^\circ)$
    $= 180^\circ - \angle AC_3B_3 - \angle BC_3A_3 = \mathbf{\angle A_3C_3B_3}$！
    顶点角严格相等：$\angle A_2C_2B_2 = \angle A_3C_3B_3$

## 步骤 5：⑤ 轮换对称性与最终结论

由几何构型的完全轮换对称性，同理可得其余两对内角对应相等：
    $\angle B_2A_2C_2 = \angle B_3A_3C_3$
    $\angle C_2B_2A_2 = \angle C_3B_3A_3$
    两三角形的三组内角对应相等，从而最终得证：
    
      $\triangle A_2B_2C_2 \sim \triangle A_3B_3C_3$
