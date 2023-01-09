import {Component, OnInit} from '@angular/core';
import {AuthService} from "../services/auth.service";
import {MatDialog} from "@angular/material/dialog";
import {Router} from "@angular/router";
import {Register} from "../../Models/register";

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  constructor(
    private authService: AuthService,
    private dialog: MatDialog,
    private router: Router
  ) {
  }
  register: Register = new Register('', '')
  ngOnInit(): void {
  }
  public onSubmit() {
    this.authService.register(this.register)
  }
}
