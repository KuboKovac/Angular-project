import {Component, OnInit} from '@angular/core';
import {AuthService} from "../services/auth.service";
import {VehiclesService} from "../services/vehicles.service";
import {IVehicle} from "../../Models/vehicle";
import {MatDialog} from "@angular/material/dialog";
import {EditVehicleComponent} from "../edit-vehicle/edit-vehicle.component";

@Component({
  selector: 'app-vehicles',
  templateUrl: './vehicles.component.html',
  styleUrls: ['./vehicles.component.scss']
})
export class VehiclesComponent implements OnInit {

  public vehicles: IVehicle[] = []

  constructor(
    public auth: AuthService,
    public vehicleService: VehiclesService,
    private dialog: MatDialog
  ) {
  }

  ngOnInit(): void {
    this.fetchVehicles()
  }

  public deleteVehicle(id: number) {
    this.vehicleService.deleteVehicle(id).subscribe(() => {
        this.fetchVehicles()
      }
    )
  }

  private fetchVehicles() {
    this.vehicleService.getAllVehicles().subscribe(response => {
      this.vehicles = response
    })
  }

  editVehicle(id: number) {
    this.dialog.open(EditVehicleComponent, {
      data: {id: id}
    })
  }
}
