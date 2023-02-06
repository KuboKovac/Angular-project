import { Component, OnInit } from '@angular/core';
import {AuthService} from "../services/auth.service";

@Component({
  selector: 'app-vehicles',
  templateUrl: './vehicles.component.html',
  styleUrls: ['./vehicles.component.scss']
})
export class VehiclesComponent implements OnInit {

  public vehicles: number[] = [0,0,0,0,0,0,0,0,0,0,0,0]

  constructor(
    public auth: AuthService
  ) { }

  ngOnInit(): void {
  }

}
