import {Component, Inject, OnInit} from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from "@angular/material/dialog";
import {VehiclesComponent} from "../vehicles/vehicles.component";
import {VehiclesService} from "../services/vehicles.service";
import {IVehicle} from "../../Models/vehicle";
import {MessageService} from "../services/message.service";

@Component({
  selector: 'app-edit-vehicle',
  templateUrl: './edit-vehicle.component.html',
  styleUrls: ['./edit-vehicle.component.scss']
})
export class EditVehicleComponent implements OnInit {

  public id: number = 0
  public vehicle: IVehicle[] = [new class implements IVehicle {
    id = 0
    imageUrl = ''
    licensePlate = ''
    owner = ''
    vehicleBrand = ''
    vehicleModel = ''
    price = 0
    kilometers = 0
  }]

  constructor(
    public dialogRef: MatDialogRef<VehiclesComponent>,
    @Inject(MAT_DIALOG_DATA) public data: {id: number},
    private vehicleService: VehiclesService,
    private message: MessageService
  ) { }

  ngOnInit(): void {
    this.id = this.data.id
    this.getData()
  }

  public getData(){
    this.vehicleService.getVehicleById(this.id + '').subscribe(response => {
      this.vehicle = response as IVehicle[]
    })
  }
  public updateData(){
    this.vehicleService.updateVehicle(this.id, this.vehicle[0]).subscribe(() => {
      this.message.message('Vehicle updated successfully!')
    })
  }
}
