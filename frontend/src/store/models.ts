
export type AsymetryStatus = "good" | "normal" | "non-critical" | "critical";
export enum AsymetryStatusEnum {
  GOOD = "good",
  NORMAL = "normal",
  NONCRITICAL = "non-critical",
  CRITICAL = "critical",
}


export interface Asymetry {
  image_url: string
  faces: number
  result: AsymetryResult[]
}

export interface AsymetryResult {
  symmetry: number
  descrition: string
  status: AsymetryStatus
}


