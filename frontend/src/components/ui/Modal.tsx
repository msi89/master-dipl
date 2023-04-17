import React, { useState, useImperativeHandle, Ref } from "react";
import ReactDom from "react-dom";

export type DialogType = HTMLDivElement & {
  open: () => void;
  close: () => void;
};

type ModalProps = React.PropsWithChildren<{
  dismissible?: boolean;
  zIndex?: number | string;
  visible?: boolean;
  name?: string;
  setVisible?: (visible: boolean) => void;
}>;

export const BaseModal: React.FC<ModalProps> = (props) => {
  const {
    children,
    visible,
    setVisible,
    name,
    dismissible = true,
    zIndex = 20,
    ...rest
  } = props;

  const modal = React.useRef(null);

  function handleDismiss(e: React.MouseEvent) {
    const target = e.target as HTMLDivElement;
    if (dismissible && target.id && target.id === name) {
      if (setVisible) setVisible(false);
    }
  }

  return  <div
      {...rest}
      className={`fixed top-0 right-0 bottom-0 left-0 flex items-center transition-opacity-visibility ease-in-out duration-300  outline-0 bg-black/60
       ${visible ? " visible opacity-100" : "invisible opacity-0"}`}
      ref={modal}
      id={name}
      onClick={handleDismiss}
      style={{ zIndex: zIndex }}
    >
      <div
        className={`relative m-auto transition-opacity-visibility-transform ease-in-out duration-300 flex flex-col outline-none ${
          visible
            ? "visible translate-y-0 scale-100 opacity-100"
            : "invisible opacity-0 scale-50 "
        }`}
      >
        {children} 
      </div>
    </div>
};

export  const Modal: React.FC<ModalProps> = (props) => {
  const { children, ...rest } = props;
  return ReactDom.createPortal(<BaseModal {...rest}>{children}</BaseModal>,
  document.body
);
}