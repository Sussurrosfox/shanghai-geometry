# 例 7 几何分步演示规划：凸四边形与相似三角形同一法证明

## 题目回顾
在凸四边形 $ABCD$ 内部有一点 $M$，满足 $MA = MC$，$\angle AMB = \angle MAD + \angle MCD$，$\angle CMD = \angle MCB + \angle MAB$。  
证明：$AB \cdot CM = BC \cdot MD$。

---

## 分步规划（共 6 步：Step 0 ~ Step 5）

### Step 0: ⓪ 已知条件与初始构型
- **标题**：⓪ 已知条件与初始构型
- **讲解正文**：
  在凸四边形 $ABCD$ 内部有一点 $M$，连接 $MA, MB, MC, MD$ 与对角线 $AC$。已知点 $M$ 满足等长条件 $MA = MC$，且位于 $\triangle ACD$ 内部。已知两个角关系：$\angle AMB = \angle MAD + \angle MCD$ 以及 $\angle CMD = \angle MCB + \angle MAB$。求证：$AB \cdot CM = BC \cdot MD$。
- **画面图元**：
  - 基础图形：凸四边形 $ABCD$（黑灰边框），对角线 $AC$（淡灰虚线），内部点 $M$，线段 $MA, MB, MC, MD$。
  - 动态元素：等长线段 $MA, MC$ 标注等长标记（红色短线），顶点 $A, B, C, D, M$ 标签。

### Step 1: ① 周角代换导出对角关系
- **标题**：① 周角代换导出对角关系
- **讲解正文**：
  考察四边形 $ABCM$ 的内角和为 $360^\circ$：$\angle MCB + \angle MAB = 360^\circ - \angle AMC - \angle ABC$。  
  代入已知条件 $\angle CMD = \angle MCB + \angle MAB$，得 $\angle CMD = 360^\circ - \angle AMC - \angle ABC$，移项即得 $\angle ABC = 360^\circ - \angle AMC - \angle CMD$。  
  另一方面，点 $M$ 处围绕周角有 $\angle AMD + \angle CMD + \angle AMC = 360^\circ$，因此 $360^\circ - \angle AMC - \angle CMD = \angle AMD$。立得：  
  $$\angle ABC = \angle AMD$$  
  同理，考察四边形 $ADCM$ 的内角和及围绕点 $M$ 的周角关系，同理可得：  
  $$\angle ADC = \angle BMC$$
- **画面图元**：
  - 动态元素：用蓝色角弧高亮相等的一对角 $\angle ABC$ 与 $\angle AMD$；用橙色角弧高亮另一对相等的角 $\angle ADC$ 与 $\angle BMC$。

### Step 2: ② 构造辅助相似 $\triangle AMD' \sim \triangle CBA$
- **标题**：② 构造辅助相似 $\triangle AMD' \sim \triangle CBA$
- **讲解正文**：
  采用同一法构造：在射线 $MD$ 上取点 $D'$，使得 $\angle MAD' = \angle ACB$。  
  结合第 ① 步已证明的 $\angle AMD' = \angle AMD = \angle ABC$，在 $\triangle AMD'$ 与 $\triangle CBA$ 中，已有两组对应角分别相等：  
  $\angle MAD' = \angle ACB$ 且 $\angle AMD' = \angle ABC$。  
  由两角对应相等，可得相似三角形：  
  $$\triangle AMD' \sim \triangle CBA$$
- **画面图元**：
  - 动态元素：在射线 $MD$ 上标出辅助点 $D'$，半透明填充高亮 $\triangle AMD'$（紫色）与 $\triangle CBA$（蓝色）；高亮对应边与对应角弧（$\angle MAD' = \angle ACB$）。

### Step 3: ③ 导出第二对相似 $\triangle D'AC \sim \triangle MCB$
- **标题**：③ 导出第二对相似 $\triangle D'AC \sim \triangle MCB$
- **讲解正文**：
  由 $\triangle AMD' \sim \triangle CBA$ 的对应角相等得 $\angle D'AM = \angle ACB$。  
  因此 $\angle D'AC = \angle D'AM + \angle MAC = \angle ACB + \angle MCA = \angle MCB$。  
  同时由相似比可知：$\frac{D'A}{AC} = \frac{AM}{CB}$。  
  代入题设等长条件 $AM = CM$，立得 $\frac{D'A}{AC} = \frac{CM}{CB}$，即 $\frac{D'A}{CM} = \frac{AC}{CB}$。  
  在 $\triangle D'AC$ 与 $\triangle MCB$ 中，两组对应边成比例且夹角相等（SAS），得第二对相似三角形：  
  $$\triangle D'AC \sim \triangle MCB$$
- **画面图元**：
  - 动态元素：半透明填充高亮 $\triangle D'AC$（绿色）与 $\triangle MCB$（黄色/橙色）；标注对应夹角 $\angle D'AC$ 与 $\angle MCB$ 相等；高亮成比例的边。

### Step 4: ④ 同一法确定点 $D'$ 与 $D$ 重合
- **标题**：④ 同一法确定点 $D'$ 与 $D$ 重合
- **讲解正文**：
  由 $\triangle D'AC \sim \triangle MCB$ 的对应角相等，得：  
  $$\angle AD'C = \angle CMB$$  
  结合第 ① 步已导出的 $\angle CMB = \angle ADC$，立得：  
  $$\angle AD'C = \angle ADC$$  
  由于点 $D'$ 位于射线 $MD$ 上，点 $D'$ 与点 $D$ 对线段 $AC$ 具有相同的张角且位于同一侧，因此点 $D'$ 必然与点 $D$ 重合（$D' \equiv D$）！  
  由此确立核心相似：  
  $$\triangle AMD \sim \triangle CBA$$
- **画面图元**：
  - 动态元素：动态动画/文字提示 $D' \equiv D$，高亮圆弧或角弧 $\angle AD'C = \angle ADC$，核心相似三角形 $\triangle AMD$ 与 $\triangle CBA$ 强化高亮（外框闪烁/双色边）。

### Step 5: ⑤ 比例变形得出最终结论
- **标题**：⑤ 比例变形得 $AB \cdot CM = BC \cdot MD$
- **讲解正文**：
  因为 $\triangle AMD \sim \triangle CBA$，对应边成比例：  
  $$\frac{AM}{CB} = \frac{MD}{AB} \implies AB \cdot AM = BC \cdot MD$$  
  最后将题设条件 $AM = CM$ 代入上式，立即得出所求的几何比例恒等式：  
  $$AB \cdot CM = BC \cdot MD$$  
  命题获证。
- **画面图元**：
  - 动态元素：高亮目标乘积的四条线段：$AB$ 与 $CM$（蓝色粗线），$BC$ 与 $MD$（红色粗线）；绘制显眼的等式结论卡片，圆满完成证明。
