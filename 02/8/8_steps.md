# 8 — 分步证明文字

## 步骤 0：⓪ 已知条件与初始构型

在凸四边形 ABCD 内部有一点 M，满足等长条件 MA = MC。
           点 M 位于 △ACD 内部，满足两个角恒等式：
           1. ∠AMB = ∠MAD + ∠MCD
           2. ∠CMD = ∠MCB + ∠MAB
           求证：AB · CM = BC · MD。

## 步骤 1：① 周角代换导出对角关系

考察四边形 ABCM 的内角和为 360°：
           ∠MCB + ∠MAB = 360° - ∠AMC - ∠ABC。
           代入已知条件 ∠CMD = ∠MCB + ∠MAB，得：
           ∠ABC = 360° - ∠AMC - ∠CMD。
           围绕点 M 周角有 ∠AMD + ∠CMD + ∠AMC = 360°，立得：
           ∠ABC = ∠AMD。
           同理考察四边形 ADCM 内角和与围绕点 M 的周角，可得：
           ∠ADC = ∠BMC。

## 步骤 2：② 构造辅助相似 △AMD' ∽ △CBA

采用同一法证明：
           在射线 MD 上取点 D'，使得 ∠MAD' = ∠ACB。
           结合第 ① 步已证明的 ∠AMD' = ∠AMD = ∠ABC，在 △AMD' 与 △CBA 中，两组对应角分别相等：
           △AMD' ∽ △CBA (AA相似)。

## 步骤 3：③ 导出第二对相似 △D'AC ∽ △MCB

由 △AMD' ∽ △CBA 得对应角相等：∠D'AM = ∠ACB。
           由于射线 AC 位于两角内部：
           ∠D'AC = ∠D'AM + ∠MAC = ∠ACB + ∠MCA = ∠MCB。
           又由相似比 D'A / AC = AM / CB，代入已知条件 AM = CM：
           D'A / AC = CM / CB ⟹ D'A / CM = AC / CB。
           两边成比例且夹角相等（SAS），得第二对相似：
           △D'AC ∽ △MCB。

## 步骤 4：④ 同一法确定点 D' 与 D 重合

由相似 △D'AC ∽ △MCB 的对应角相等，得：
           ∠AD'C = ∠CMB。
           结合第 ① 步已导出的 ∠CMB = ∠ADC，立得：
           ∠AD'C = ∠ADC。
           因点 D' 位于射线 MD 上，且点 D' 与 D 对线段 AC 的张角相同且位于同侧，故点 D' 必与 D 重合（D' ≡ D）！
           由此正式确立核心相似：
           △AMD ∽ △CBA。

## 步骤 5：⑤ 比例变形得出最终结论

由核心相似 △AMD ∽ △CBA，对应边成比例：
           AM / CB = MD / AB ⟹ AB · AM = BC · MD。
           最后利用已知条件 AM = CM 代换，立即得出：
           
             AB · CM = BC · MD
           
           命题获证！
