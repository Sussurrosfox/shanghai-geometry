# 例 7 分步演示规划 (steps.md)

## 题目概述
设 $O, H$ 分别是锐角 $\triangle ABC$ 的外心和垂心，证明：在边 $BC, CA, AB$ 上分别存在点 $D, E, F$，使得 $OD + DH = OE + EH = OF + FH$ 且 $AD, BE, CF$ 三线共点。

---

## 步骤规划

### Step 0: 构型与外心/垂心
- **标题**：已知条件与几何构型
- **正文**：
  给定锐角 $\triangle ABC$，其外心为 $O$（外接圆半径为 $R$），垂心为 $H$（三条高线的交点）。<br>
  求证：在边 $BC, CA, AB$ 上存在点 $D, E, F$，使折线长 $OD+DH = OE+EH = OF+FH$，且 $AD, BE, CF$ 三线共点。
- **画面**：
  - 绘制锐角 $\triangle ABC$ 及其外接圆 $\odot O$。
  - 标出外心 $O$ 与垂心 $H$。
  - 绘制三条高线虚线（高线垂足），清晰展示 $H$ 的几何含义。
- **颜色约定**：
  - $\triangle ABC$：深灰/深蓝边框 (`#1e293b`)
  - 外接圆 $\odot O$：浅蓝灰色细线 (`#64748b`)
  - 外心 $O$：蓝色 (`#2563eb`)
  - 垂心 $H$：红色 (`#dc2626`)

---

### Step 1: 垂心对称点落在外接圆上
- **标题**：垂心关于三边的对称点均在外接圆上
- **正文**：
  设垂心 $H$ 关于三边 $BC, CA, AB$ 的对称点分别为 $A', B', C'$。<br>
  由垂心的经典性质：$\angle BHC = 180^\circ - \angle A$；因为 $A'$ 与 $H$ 关于 $BC$ 对称，故 $\angle BA'C = \angle BHC = 180^\circ - \angle A$。<br>
  四边形 $AB A' C$ 对角互补，故 $A'$ 落在 $\triangle ABC$ 的外接圆 $\odot O$ 上！同理，$B', C'$ 亦均落在外接圆 $\odot O$ 上。
- **画面**：
  - 擦除 Step 0 的高线虚线。
  - 画出垂心 $H$ 到三边的垂足引线及对称线段 $HA', HB', HC'$（虚线）。
  - 点亮外接圆上的三个对称点 $A', B', C'$。
  - 突出显示 $A', B', C'$ 位于圆周上的几何事实。
- **颜色约定**：
  - 对称虚线 $HA', HB', HC'$：淡红色虚线
  - 对称点 $A', B', C'$：紫色 (`#7c3aed`)

---

### Step 2: 射线连结定三点，折线长恒等于 R
- **标题**：射线 $OA', OB', OC'$ 确定 $D, E, F$ 且折线长恒等于 $R$
- **正文**：
  连结圆心 $O$ 与外接圆上各对称点，设线段 $OA'$ 与 $BC$ 交于 $D$，$OB'$ 与 $CA$ 交于 $E$，$OC'$ 与 $AB$ 交于 $F$。<br>
  由对称性可知 $DH = DA'$，因此折线长：<br>
  <span style="color:#059669;font-weight:bold;">$OD + DH = OD + DA' = OA' = R$</span>（其中 $R$ 为外接圆半径）。<br>
  同理，<span style="color:#059669;font-weight:bold;">$OE + EH = OB' = R$</span>，<span style="color:#059669;font-weight:bold;">$OF + FH = OC' = R$</span>。<br>
  第一组等式条件天然获证！
- **画面**：
  - 连结半径线段 $OA', OB', OC'$。
  - 标出三边上的交点 $D, E, F$。
  - 高亮折线段 $OD$ 与 $DH$（并由等长虚线 $DA'$ 揭示 $DH = DA'$，折线伸直为半径 $OA'=R$）。
  - 标出 $OE, EH$ 与 $OF, FH$ 的折线等长效果。
- **颜色约定**：
  - 点 $D, E, F$：绿色 (`#059669`)
  - 半径段 $OA', OB', OC'$：青色/绿色
  - 折线高亮：翡翠绿 (`#059669`)

---

### Step 3: 外心射线交点与对称全等三角形
- **标题**：外心射线交点 $D', E', F'$ 与全等对称关系
- **正文**：
  引辅助射线：设直线 $AO, BO, CO$ 与三边 $BC, CA, AB$ 分别交于 $D', E', F'$。<br>
  在圆周与角关系中，$\angle BAO = 90^\circ - \angle ACB = \angle CAA'$，由此推得圆心角 <span style="color:#2563eb;font-weight:bold;">$\angle BOD' = \angle COD$</span>。<br>
  又在等腰 $\triangle OBC$ 中 $OB = OC$，底角 $\angle OBD' = \angle OCD = 90^\circ - \angle A$。<br>
  由角边角 (ASA) 判定得全等：<span style="color:#ea580c;font-weight:bold;">$\triangle OBD' \cong \triangle OCD$</span>！<br>
  于是对应边相等：<span style="color:#ea580c;font-weight:bold;">$BD' = CD$</span>。同理可得 <span style="color:#ea580c;font-weight:bold;">$CE' = AE$</span>，<span style="color:#ea580c;font-weight:bold;">$AF' = BF$</span>。
- **画面**：
  - 绘制外心射线 $AD', BE', CF'$，标出点 $D', E', F'$。
  - 用半透明色块填充高亮全等三角形 $\triangle OBD'$ 与 $\triangle OCD$。
  - 标记底角 $\angle OBD' = \angle OCD$ 及顶角 $\angle BOD' = \angle COD$。
  - 用等长标记直观标出 $BD' = CD$。
- **颜色约定**：
  - 点 $D', E', F'$：橙色 (`#ea580c`)
  - 全等三角形填充：橙色半透明 (`rgba(234, 88, 12, 0.18)`)
  - 等长刻度线：橙色 (`#ea580c`)

---

### Step 4: 塞瓦定理比值代换
- **标题**：对外心 $O$ 应用塞瓦定理并完成线段比值代换
- **正文**：
  因为射线 $AD', BE', CF'$ 共点于外心 $O$，对 $\triangle ABC$ 与点 $O$ 应用塞瓦定理，得：<br>
  $$\frac{BD'}{D'C} \cdot \frac{CE'}{E'A} \cdot \frac{AF'}{F'B} = 1$$<br>
  利用 Step 3 证得的等长关系 $BD' = CD$（故 $D'C = a - BD' = a - CD = DB$），以及 $CE' = AE, E'A = EC$，$AF' = BF, F'B = FA$，代入上式即得：<br>
  <span style="color:#2563eb;font-weight:bold;">$$\frac{CD}{DB} \cdot \frac{AE}{EC} \cdot \frac{BF}{FA} = 1 \iff \frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = 1$$</span>
- **画面**：
  - 保留 $D, E, F$ 与三边线段分割示意。
  - 高亮显示三边上的对应分段 $CD$ 与 $DB$、$AE$ 与 $EC$、$BF$ 与 $FA$。
  - 对应线段着色对比，使塞瓦比值的分子与分母对应关系一目了然。
- **颜色约定**：
  - 分段对比色：蓝色 (`#2563eb`) 与紫色 (`#7c3aed`)

---

### Step 5: 逆定理得证三线共点
- **标题**：由塞瓦定理逆定理得 $AD, BE, CF$ 三线共点
- **正文**：
  因为 $D, E, F$ 分别是边 $BC, CA, AB$ 上的内分点，且满足塞瓦比值恒等式：<br>
  $$\frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = 1$$<br>
  由<b>塞瓦定理逆定理</b>，直线 <span style="color:#dc2626;font-weight:bold;">$AD, BE, CF$ 必三线共点于点 $K$</span>！<br>
  至此，存在点 $D, E, F$ 满足折线长相等且三线共点全部获证。
- **画面**：
  - 连结直线 $AD, BE, CF$ 并高亮加粗。
  - 显现三线交点 $K$（闪烁光晕/醒目大圆点）。
  - 全局视觉达到最终高潮，结论清晰明朗。
- **颜色约定**：
  - 共线 $AD, BE, CF$：深红/金红高亮 (`#dc2626`, `#b91c1c`)
  - 共点 $K$：红金色光晕 (`#e11d48`)
