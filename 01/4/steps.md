# 例 3 分步证明规划

## 命题陈述
在 $\bigtriangleup ABC$ 中，$AB < AC$。过点 $B$ 平行于 $AC$ 的直线交 $\angle BAC$ 的外角平分线于点 $D$，过点 $C$ 平行于 $AB$ 的直线交这条角平分线于 $E$。点 $F$ 是 $AC$ 上一点，使得 $FC = AB$。
证明：$DF = FE$。

---

## 演示分步设计

### 步骤 0：已知条件与几何构型
- **标题**：✦ 已知条件与几何图形
- **正文**：在 $\bigtriangleup ABC$ 中，$AB < AC$。直线 $DE$ 为 $\angle BAC$ 的外角平分线。过点 $B$ 作 $BD \parallel AC$ 交外角平分线于 $D$，过点 $C$ 作 $CE \parallel AB$ 交外角平分线于 $E$。在边 $AC$ 上取一点 $F$，使得 $FC = AB$。求证：$DF = FE$。
- **画面**：
  - 基础三角形 $ABC$（深色实线）。
  - 外角平分线直线 $DE$（深灰虚线贯穿 $D, A, E$）。
  - 平行线段 $BD$ 与 $CE$。
  - 点 $F$ 位于线段 $AC$ 上。
  - 顶点标签 $A, B, C, D, E, F$。

### 步骤 1：延长辅助线构造平行四边形 ABGC
- **标题**：① 延长 DB、EC 交于点 G，连接 GF
- **正文**：延长 $DB$ 与 $EC$ 交于点 $G$，连接 $GF$。<br>由作图条件可知：$DG \parallel AC$（即 $BG \parallel AC$），$EG \parallel AB$（即 $CG \parallel AB$）。<br>两组对边分别平行，因此四边形 $ABGC$ 是**平行四边形**。
- **画面**：
  - 显现辅助顶点 $G$ 及其标签。
  - 延长虚线段 $BG$ 与 $CG$ 至点 $G$。
  - 连结辅助虚线段 $GF$。
  - 平行四边形 $ABGC$ 边缘高亮（青色微光），标出对边平行箭头。

### 步骤 2：证明 △DEG 为等腰三角形 (DG = GE)
- **标题**：② 外角平分线与平行线性质 ⇒ DG = GE
- **正文**：由 $EG \parallel AB$，直线 $DE$ 为截线，得内错角 $\angle DEG = \angle DAB$；<br>同理由 $DG \parallel AC$，截线 $DE$ 给出内错角 $\angle ADG = \angle EAC$。<br>因为 $DE$ 是 $\angle BAC$ 的外角平分线，由对称性知两旁与三角形两边的夹角相等：$\angle DAB = \angle EAC$。<br>从而 $\angle DEG = \angle ADG$。在 $\bigtriangleup DEG$ 中两底角相等，故为等腰三角形，即 **$DG = GE$**。
- **画面**：
  - 标出四组等角弧：$\angle DAB, \angle EAC, \angle DEG, \angle ADG$（同一明亮蓝色）。
  - 高亮显示大等腰三角形 $\bigtriangleup DEG$ 的两腰 $DG$ 与 $EG$（加双刻度线标记）。

### 步骤 3：利用平行四边形转化条件证明 CG = CF
- **标题**：③ 平行四边形对边相等转化 ⇒ CG = CF
- **正文**：在平行四边形 $ABGC$ 中，对边相等得 $CG = AB$。<br>又题设已知条件为 $CF = AB$，等量代换立即得到 **$CG = CF$**。<br>因此 $\bigtriangleup CGF$ 是以 $C$ 为顶点的等腰三角形，其两底角相等：$\angle CGF = \angle CFG$。
- **画面**：
  - 高亮三条等长线段 $AB$、$CG$、$CF$（绿色粗实线加单刻度线）。
  - 浅绿色半透明填充等腰 $\bigtriangleup CGF$。
  - 标出两底角弧 $\angle CGF$ 与 $\angle CFG$（绿色角弧）。

### 步骤 4：内错角代换得出 GF 平分 ∠DGE
- **标题**：④ 内错角转化得出 GF 为 ∠DGE 的角平分线
- **正文**：因为 $BG \parallel AC$，以 $GF$ 为截线得内错角相等：$\angle FGB = \angle CFG$。<br>结合步骤 3 的等腰底角关系 $\angle CGF = \angle CFG$，推得：$\angle FGB = \angle CGF$。<br>注意到点 $B$ 在线段 $GD$ 上，点 $C$ 在线段 $GE$ 上，故 $\angle FGD = \angle FGB$，$\angle FGE = \angle CGF$。<br>从而 **$\angle FGD = \angle FGE$**，即射线 $GF$ 为顶角 $\angle DGE$ 的角平分线！
- **画面**：
  - 高亮内错角 $\angle CFG$ 与 $\angle FGB$（紫色角弧）。
  - 动态显示对顶角平分关系：强调 $\angle FGD$ 与 $\angle FGE$ 互等（高亮双角弧）。
  - 高亮轴对称中心线 $GF$（紫色虚线发光）。

### 步骤 5：全等三角形判定与得出最终结论
- **标题**：⑤ SAS 判定 △DFG ≌ △EFG ⇒ DF = FE
- **正文**：在 $\bigtriangleup DFG$ 与 $\bigtriangleup EFG$ 中：<br>① $DG = GE$（步骤 2 已证）；<br>② $\angle FGD = \angle FGE$（步骤 4 已证）；<br>③ $FG = FG$（公共边）。<br>由**边角边（SAS）**全等判定定理，可得 **$\bigtriangleup DFG \cong \bigtriangleup EFG$**。<br>全等三角形对应边相等，故 **$DF = FE$**。命题得证！
- **画面**：
  - 半透明高亮填充两全等三角形 $\bigtriangleup DFG$（浅蓝色）与 $\bigtriangleup EFG$（浅橙色）。
  - 连接并高亮目标线段 $DF$ 与 $EF$（红色加粗发光实线，附三刻度线标记）。
  - 全屏呈现证明收官结论卡片。
