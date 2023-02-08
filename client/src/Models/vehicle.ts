export interface IVehicle{
  id: number,
  imageUrl: string,
  licensePlate: string,
  owner: string,
  vehicleBrand: string,
  vehicleModel: string,
  price?: number,
  kilometers?: number
}
