
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
  measure: FaceMeasure[]
}

export interface AsymetryResult {
  symmetry: number
  descrition: string
  status: AsymetryStatus
}


export interface FaceMeasure {
  horizontal_asymmetry: number
  vertical_asymmetry: number
  proportionality: number
  face_width: number
  face_height: number
  left_eye_width: number
  right_eye_width: number
  nose_width: number
  mouth_width: number
}

