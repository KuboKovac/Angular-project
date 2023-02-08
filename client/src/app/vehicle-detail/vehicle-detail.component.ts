import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {VehiclesService} from "../services/vehicles.service";
import {IVehicle} from "../../Models/vehicle";

@Component({
  selector: 'app-vehicle-detail',
  templateUrl: './vehicle-detail.component.html',
  styleUrls: ['./vehicle-detail.component.scss']
})
export class VehicleDetailComponent implements OnInit {

  declare private id: string | null
  declare public vehicle: IVehicle[]

  constructor(
    private activatedRoute: ActivatedRoute,
    private vehicleService: VehiclesService
  ) { }

  ngOnInit(): void {
    this.activatedRoute.paramMap.subscribe(() => {
      this.id = this.activatedRoute.snapshot.paramMap.get('id')
      this.vehicleService.getVehicleById(this.id).subscribe(response => {
        this.vehicle = response
        console.log(response)
      })
    })
  }

}
