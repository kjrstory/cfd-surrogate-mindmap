// src/components/MindMap.types.ts

/** 각 Method(논문/모델)의 상세 정보 */
export interface MethodDetail {
  year: number;
  source: string;
  scenario: string[];
  doi: string | null;
  codeUrl: string | null;
}

/** GridType 레벨: Method 이름 → 상세 정보 */
export interface GridLevel {
  [method: string]: MethodDetail;
}

/** Backbone 레벨: GridType 이름 → GridLevel */
export interface BackboneLevel {
  [gridType: string]: GridLevel;
}

/** 최상위 트리: Backbone 이름 → BackboneLevel */
export type TreeData = Record<string, BackboneLevel>;
