# 7 — 分步证明文字

## 步骤 0：已知条件与凸六边形

在凸六边形 ABCDEF 中，已知两组对应边相等：
           • AB = CD = EF（图中双杠标记）
           • BC = DE = FA（图中单杠标记）
           角满足和关系：
           
             ∠FAB + ∠ABC = ∠FAB + ∠EFA = 240°
           
           求证：∠FAB + ∠CDE = 240°。

## 步骤 1：① 连接对角线并导出 ∠ABC = ∠EFA

连接三条对角线 AC, CE, EA（紫色虚线）。
           由题目已知条件：
           
             ∠FAB + ∠ABC = 240°
             ∠FAB + ∠EFA = 240°
           
           两式同时减去公共角 ∠FAB，立即可得：
           
             ∠ABC = ∠EFA
           
           由此将两处顶角建立等量联系。

## 步骤 2：② 证明 △ABC ≌ △EFA

在 △ABC 与 △EFA 中：
           • AB = EF（已知对应边相等）
           • ∠ABC = ∠EFA（Step 1 已证）
           • BC = FA（已知对应边相等）
           由边角边（SAS）全等判定：
           
             △ABC ≌ △EFA
           
           由此得出对应边与对应角相等：
           
             AC = AE，且 ∠BAC = ∠FEA（记为 α）

## 步骤 3：③ 角度代换求得 ∠EAC = 60°

观察顶点 A 处的内角拆分：
           
             ∠EAC = ∠FAB - ∠FAE - ∠BAC
           
           代入 Step 2 全等所得对应角 ∠BAC = ∠FEA：
           
             ∠EAC = ∠FAB - (∠FAE + ∠FEA)
           
           在 △EFA 中，两内角和 ∠FAE + ∠FEA = 180° - ∠EFA，代入得：
           
             ∠EAC = ∠FAB - (180° - ∠EFA)
                   = (∠FAB + ∠EFA) - 180°
                   = 240° - 180° = 60°

## 步骤 4：④ 判定 △ACE 是正三角形

综合前面的几何结论：
           • 由 Step 2 知：AC = AE（等腰）
           • 由 Step 3 算得顶角：∠EAC = 60°
           有一个角是 60° 的等腰三角形必为正三角形：
           
             △ACE 是正三角形（等边三角形）
           
           因此三边对角线完全等长：
           
             AC = CE = EA

## 步骤 5：⑤ △ABC ≌ △CDE 推出最终结论

比较 △ABC 与 △CDE 的三条边长：
           • AB = CD（已知条件）
           • BC = DE（已知条件）
           • AC = CE（Step 4 已证正三角形边长）
           由边边边（SSS）全等判定：
           
             △ABC ≌ △CDE
           
           从而对应角相等：∠ABC = ∠CDE。
           代入已知等式：
           
             ∠FAB + ∠CDE = ∠FAB + ∠ABC = 240°
           
           原命题获证！
