
export type AsymetryStatus = "good" | "normal" | "warning" | "critical";
export enum AsymetryStatusEnum {
  GOOD = "forward",
  NORMAL = "back",
  WARNING = "none",
  CRITICAL = "none",
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


