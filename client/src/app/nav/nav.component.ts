import { Component, OnInit } from '@angular/core';
import {MatDialog} from "@angular/material/dialog";
import {LoginComponent} from "../login/login.component";
import {RegisterComponent} from "../register/register.component";
import {AddVehicleComponent} from "../add-vehicle/add-vehicle.component";
import {AuthService} from "../services/auth.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.scss']
})
export class NavComponent implements OnInit {

  constructor(private dialog: MatDialog,
              public authService: AuthService,
              private router: Router) { }

  ngOnInit(): void {}

  public openLogin(){
    this.dialog.open(LoginComponent)
  }

  public openRegister(){
    this.dialog.open(RegisterComponent)
  }

  logout() {
    this.authService.logout()
    this.router.navigateByUrl('/home')
  }
}
