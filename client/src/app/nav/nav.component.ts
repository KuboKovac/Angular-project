import { Component, OnInit } from '@angular/core';
import {MatDialog} from "@angular/material/dialog";
import {LoginComponent} from "../login/login.component";
import {RegisterComponent} from "../register/register.component";

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.scss']
})
export class NavComponent implements OnInit {

  constructor(private dialog: MatDialog) { }

  ngOnInit(): void {}

  public openLogin(){
    this.dialog.open(LoginComponent)
  }

  public openRegister(){
    this.dialog.open(RegisterComponent)
  }
}
