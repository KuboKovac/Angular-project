import { Component, OnInit } from '@angular/core';
import {VehiclesService} from "../services/vehicles.service";
import {IVehicle} from "../../Models/vehicle";
import {FormControl, FormGroup, Validators} from "@angular/forms";
import {MessageService} from "../services/message.service";

@Component({
  selector: 'app-add-vehicle',
  templateUrl: './add-vehicle.component.html',
  styleUrls: ['./add-vehicle.component.scss']
})
export class AddVehicleComponent implements OnInit {

  public vehicle: IVehicle = new class implements IVehicle {
    id = 0
    imageUrl = ''
    licensePlate = ''
    owner = ''
    vehicleBrand = ''
    vehicleModel = ''
    price = 0
    kilometers = 0
  }
  vehicleForm = new FormGroup({
    name: new FormControl('',[Validators.required]),
    brand: new FormControl('',[Validators.required]),
    licensePlate: new FormControl('',[Validators.required]),
    owner: new FormControl('',[Validators.required]),
    pictureUrl: new FormControl('',[Validators.required]),
    price: new FormControl('',[Validators.required]),
    km: new FormControl('',[Validators.required])
  })
  constructor(
    private vehicleService: VehiclesService,
    private msgService: MessageService
  ) { }

  ngOnInit(): void {
  }

  public addVehicle(){
    this.vehicleService.addVehicle(this.vehicle).subscribe(next => {
      this.msgService.message('Vehicle added successfully!', 3000)
    })
  }

}
